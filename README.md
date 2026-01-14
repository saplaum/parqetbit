# Bitvavo to Parqet Converter

## Description
A Python script to convert Bitvavo transaction export CSVs into a format compatible with Parqet for portfolio tracking.

## Features
- Converts 'Buy' transactions from Bitvavo CSV to Parqet import format.
- Handles date/time formatting for Parqet's `datetime` field.
- Adjusts numeric decimal separators from `.` to `,` as required by Parqet.
- Maps relevant Bitvavo transaction details to Parqet's expected fields (currency, date, price, shares, etc.).

## How to Use

### 1. Export Data from Bitvavo
Export your transaction history from Bitvavo as a CSV file. Ensure the file is named `bitvavo.csv` and placed in the same directory as the script.

### 2. Run the Conversion Script
Execute the Python script:
```bash
python convert_bitvavo_to_parqet.py
```

### 3. Import into Parqet
A new file named `parqet_import.csv` will be generated. You can then import this file into Parqet.

## Requirements
- Python 3.x (standard library only, no external packages needed)

## Limitations
- Currently only processes 'Buy' transactions. Other transaction types (e.g., 'Sell', 'Deposit', 'Withdrawal') are ignored.
- Assumes Bitvavo transaction times are in a local timezone and formats them as UTC ('Z' suffix) without explicit timezone conversion. For precise timezone handling, modifications would be required.

## License
This project is licensed under the [LICENSE](LICENSE) file.
