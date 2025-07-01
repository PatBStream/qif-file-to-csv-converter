import csv
import argparse
from datetime import datetime

def parse_qif(input_file, text_output_file, csv_output_file):
    try:
        # Open the QIF file for reading
        with open(input_file, 'r') as qif_file:
            transactions = []
            transaction = {}
            account_type = None

            # Read each line in the QIF file
            for line in qif_file:
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Detect account type
                if line.startswith("!Type:"):
                    account_type = line.split(":")[1]
                    continue

                # Parse transaction details
                if line.startswith("D"):  # Date
                    raw_date = line[1:]
                    dt = None
                    # Try common QIF date formats: MM/DD/YYYY, MM/DD'YYYY, YYYYMMDD
                    for fmt in ("%m/%d/%Y", "%m/%d'%Y", "%Y%m%d"):  
                        try:
                            dt = datetime.strptime(raw_date, fmt)
                            break
                        except ValueError:
                            continue
                    if dt:
                        transaction["Date"] = dt.strftime("%m-%d-%Y")  # Format MM-DD-YYYY
                    else:
                        transaction["Date"] = raw_date  # Fallback as-is
                elif line.startswith("T"):  # Amount
                    transaction["Amount"] = line[1:]
                elif line.startswith("P"):  # Payee
                    transaction["Payee"] = line[1:]
                elif line.startswith("L"):  # Category
                    transaction["Category"] = line[1:]
                elif line.startswith("M"):  # Memo
                    transaction["Memo"] = line[1:]
                elif line == "^":  # End of transaction
                    # Add account type if available
                    if account_type:
                        transaction["Account Type"] = account_type
                    # Ensure all expected fields exist
                    transaction.setdefault("Date", "")
                    transaction.setdefault("Amount", "")
                    transaction.setdefault("Payee", "")
                    transaction.setdefault("Category", "")
                    transaction.setdefault("Memo", "")
                    transaction.setdefault("Account Type", "")

                    transactions.append(transaction)
                    transaction = {}
                    

        # Write to a human-readable text file
        with open(text_output_file, 'w') as txt_file:
            txt_file.write("Transactions Summary\n")
            txt_file.write("=" * 40 + "\n")
            for trans in transactions:
                txt_file.write(f"Date: {trans.get('Date', 'N/A')}\n")
                txt_file.write(f"Amount: {trans.get('Amount', 'N/A')}\n")
                txt_file.write(f"Payee: {trans.get('Payee', 'N/A')}\n")
                txt_file.write(f"Category: {trans.get('Category', 'N/A')}\n")
                txt_file.write(f"Memo: {trans.get('Memo', 'N/A')}\n")
                txt_file.write(f"Account Type: {trans.get('Account Type', 'N/A')}\n")
                txt_file.write("-" * 40 + "\n")

        # Write to a CSV file
        with open(csv_output_file, 'w', newline='') as csv_file:
            fieldnames = ["Date", "Amount", "Payee", "Category", "Memo", "Account Type"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for trans in transactions:
                writer.writerow({
                    "Date": trans.get("Date", ""),
                    "Amount": trans.get("Amount", ""),
                    "Payee": trans.get("Payee", ""),
                    "Category": trans.get("Category", ""),
                    "Memo": trans.get("Memo", ""),
                    "Account Type": trans.get("Account Type", ""),
                })

        print(f"Parsing completed successfully. Output written to:\n- {text_output_file}\n- {csv_output_file}")
    except Exception as e:
        print(f"Error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="Parse a QIF file and output a summary and CSV.")
    parser.add_argument(
        '-i', '--input',
        dest='input_file',
        required=True,
        help='Path to the input QIF file'
    )
    parser.add_argument(
        '-t', '--text-output',
        dest='text_output',
        default='transactions_summary.txt',
        help='Path for the human-readable summary file (default: transactions_summary.txt)'
    )
    parser.add_argument(
        '-c', '--csv-output',
        dest='csv_output',
        default='transactions.csv',
        help='Path for the output CSV file (default: transactions.csv)'
    )

    args = parser.parse_args()
    parse_qif(args.input_file, args.text_output, args.csv_output)

if __name__ == '__main__':
    main()
