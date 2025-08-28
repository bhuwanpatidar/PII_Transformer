# PII Detection and Redaction Tool

## Overview
This Python program detects Personally Identifiable Information (PII) in text files and redacts or masks the sensitive data. The program scans through the input files, identifies potential PII such as names, addresses, phone numbers, email addresses, and other sensitive information, and replaces it with placeholders to ensure privacy.

## Features
- **PII Detection**: Detects a wide range of PII such as names, email addresses, phone numbers, SSNs, credit card numbers, etc.
- **Redaction/Masking**: Replaces detected PII with placeholders or masked versions (e.g., `********` or `****`).
- **Input and Output**: Accepts input text files and generates new files with redacted information.
- **Customizable Redaction**: Users can define what constitutes PII and how it should be redacted/masked.

## Requirements
- Python 3.x
- Libraries Used :- sys,json and csv

