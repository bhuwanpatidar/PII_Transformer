import csv
import json
import sys


files = sys.argv[1]
output = 'updated_data.csv'


sensitive_keys = {
    "phone": 6,
    "aadhar": 8,
    "passport": 5,
    "upi_id": 4,
    "email": 4,
    "address": 8,
    "ip_address": 6,
    "device_id": 4
}

# function for marked data 
def mask_data(field, data):
    if field in data:
        sensitive_value = data[field]
        mask_length = sensitive_keys.get(field, 4)  
        masked_value = 'X' * mask_length + sensitive_value[mask_length:]
        data[field] = masked_value
        return True
    return False


def process_csv():
    with open(files, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Is_confidential']
        rows = []

        for row in reader:
            try:
                
                data_json = row['data_json'].replace('""', '"')  
                data = json.loads(data_json)

                # it will mark all the data to non confidential.
                is_confidential = False

                # hidding data 
                for field in sensitive_keys:
                    if mask_data(field, data):
                        is_confidential = True

                # hidding data with vobinations
                field_combinations = [
                    (["name", "email"], "email"),
                    (["name", "address"], "address"),
                    (["name", "ip_address"], "ip_address"),
                    (["name", "device_id"], "device_id"),
                    (["address", "email"], "address"),
                    (["device_id", "email"], "device_id"),
                    (["ip_address", "email"], "ip_address"),
                    (["ip_address", "address"], "ip_address"),
                    (["ip_address", "device_id"], "ip_address")
                ]

                for fields, mask_field in field_combinations:
                    if all(f in data for f in fields):
                        if mask_data(mask_field, data):
                            is_confidential = True

                # updating from false to true if there is confidential data
                row['Is_confidential'] = is_confidential
                row['data_json'] = json.dumps(data)

            except json.JSONDecodeError:
                print(f"Error parsing JSON in line {row.get('record_id', 'Unknown')}")
                continue

            rows.append(row)

    # writing output to new file
    with open(output, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated CSV has been saved to {output}")

# main function
if __name__ == "__main__":
    process_csv()
