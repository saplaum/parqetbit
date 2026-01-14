import csv
import datetime

def convert_bitvavo_to_parqet(input_csv_path, output_csv_path):
    parqet_data = []
    
    # Parqet CSV header
    parqet_header = [
        "currency", "date", "datetime", "fee", "fxrate", 
        "assetType", "identifier", "price", "shares", 
        "amount", "tax", "time", "type", "wkn"
    ]
    parqet_data.append(parqet_header)

    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        
        for row in reader:
            if row['Type'].lower() == 'buy':
                # Convert Bitvavo 'buy' transaction to Parqet format
                
                # Date and Time conversion
                # Bitvavo: '2026-01-14', '15:57:09.152' or '15:56:05'
                # Parqet: 'yyyy-MM-dd', 'yyyy-MM-ddTHH:mm:ss.fffZ'
                
                bitvavo_date_str = row['Date']
                bitvavo_time_str = row['Time']
                
                # Handle cases where milliseconds might be missing
                if '.' not in bitvavo_time_str:
                    bitvavo_time_str += '.000'
                
                dt_obj = datetime.datetime.strptime(
                    f"{bitvavo_date_str} {bitvavo_time_str}", 
                    "%Y-%m-%d %H:%M:%S.%f"
                )
                
                # Assuming Bitvavo times are local (Europe/Berlin) and converting to UTC for 'Z' suffix.
                # For simplicity, we are appending 'Z' directly.
                # Proper timezone handling would require pytz or similar library.
                # For now, we'll assume the displayed time is the 'event time' and format it as UTC.
                parqet_date = dt_obj.strftime("%Y-%m-%d")
                parqet_datetime = dt_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z' # [:-3] to cut to milliseconds
                
                # Numeric conversions: replace '.' with ',' and convert to positive
                # Parqet uses comma as decimal separator.
                
                # Check for empty strings before conversion
                quote_price = row.get('Quote Price', '0').replace('.', ',') if row.get('Quote Price') else '0,00'
                amount_bitvavo = row.get('Amount', '0').replace('.', ',') if row.get('Amount') else '0,00'
                received_paid_amount = row.get('Received / Paid Amount', '0').replace('.', ',') if row.get('Received / Paid Amount') else '0,00'
                fee_amount_bitvavo = row.get('Fee amount', '0').replace('.', ',') if row.get('Fee amount') else '0,00'

                parqet_row = {
                    "currency": row['Quote Currency'],
                    "date": parqet_date,
                    "datetime": parqet_datetime,
                    "fee": fee_amount_bitvavo,
                    "fxrate": "", # Not provided by Bitvavo for buy transactions
                    "assetType": "Crypto",
                    "identifier": row['Currency'],
                    "price": quote_price,
                    "shares": amount_bitvavo,
                    "amount": received_paid_amount.lstrip('-'), # Absolute value
                    "tax": "0,00",
                    "time": "", # Included in datetime
                    "type": "Buy",
                    "wkn": ""
                }
                parqet_data.append([parqet_row[key] for key in parqet_header])

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerows(parqet_data)

    print(f"Conversion complete. Parqet-compatible CSV saved to {output_csv_path}")

if __name__ == "__main__":
    convert_bitvavo_to_parqet('bitvavo.csv', 'parqet_import.csv')
