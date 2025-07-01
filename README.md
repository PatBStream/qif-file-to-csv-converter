# QIF File to CSV File Converter

[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/PatBStream/parser-qif-to-csv.svg)](https://github.com/PatBStream/parser-qif-to-csv/commits/main)
[![Issues](https://img.shields.io/github/issues/PatBStream/parser-qif-to-csv.svg)](https://github.com/PatBStream/parser-qif-to-csv/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/PatBStream/parser-qif-to-csv.svg)](https://github.com/PatBStream/parser-qif-to-csv/pulls)

Convert **Quicken Interchange Format (QIF)** files into a readable summary text file and a structured CSV file for easy analysis or Excel import.

---

## Features

* **Parses QIF files** exported from Microsoft Money, Quicken, or similar tools.
* Outputs:

  * Human-readable summary file (TXT)
  * Structured CSV file suitable for Excel or data analytics
* Automatically handles common QIF date formats and missing fields.

---

## Requirements

* Python 3.6 or newer

No extra dependencies are required (uses only Python standard library).

---

## Usage

### 1. Clone or Download

```bash
git clone <YOUR_REPO_URL>
cd <YOUR_REPO_DIR>
```

Or just download `parse-qif-to-csv.py` directly.

### 2. Run the Script

```bash
python parse-qif-to-csv.py -i <input_file.qif> [-t <summary_output.txt>] [-c <output.csv>]
```

#### Arguments

| Flag                | Description                      | Default Value             |
| ------------------- | -------------------------------- | ------------------------- |
| `-i, --input`       | Path to the input QIF file       | **(required)**            |
| `-t, --text-output` | Path to output summary text file | transactions\_summary.txt |
| `-c, --csv-output`  | Path to output CSV file          | transactions.csv          |

#### Example

```bash
python parse-qif-to-csv.py -i sample.qif -t summary.txt -c output.csv
```

---

## Output

* **TXT summary:**
  Example (`summary.txt`):

  ```
  Transactions Summary
  ========================================
  Date: 01-31-2020
  Amount: -200.00
  Payee: HOA
  Category: Fees
  Memo: Annual Dues
  Account Type: Bank
  ----------------------------------------
  ```
* **CSV file:**
  Columns: Date, Amount, Payee, Category, Memo, Account Type

---

## QIF Date Handling

* Supports dates like:

  * `MM/DD/YYYY`
  * `MM/DD'YYYY`
  * `YYYYMMDD`
* If date parsing fails, the original string is used in the output.

---

## Example QIF Input

```
!Type:Bank
D01/31/2020
T-200.00
PHOA
LFees
MAnnual Dues
^
```

---

## Troubleshooting

* If you get an error like `Error occurred: ...`, check that your input QIF file exists and is valid.
* Only standard QIF fields are parsed: **Date, Amount, Payee, Category, Memo, Account Type.**
* For large files, processing time depends on file size but is generally fast.

---

## License

MIT License.

---

## Author

* PatBStream\@GitHub

---

**Contributions, bug reports, and suggestions welcome!**
