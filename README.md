# 📊 BOM Data Validator

## 📌 Project Overview
This Python-based automation tool is designed to validate **Bill of Materials (BOM)** data stored in Excel files. In manufacturing and operational environments, manual data entry errors (such as negative costs or missing descriptions) can lead to significant production delays. This tool automates the quality assurance process for such datasets.

## 🚀 Key Features
- **Data Integrity Check:** Automatically detects missing product descriptions or null values.
- **Cost Validation:** Identifies invalid (negative) unit costs to prevent accounting errors.
- **Inventory Alert:** Flags items that have fallen below a defined safety stock level (e.g., < 10 units).
- **Automated Reporting:** Prints a summary of errors and warnings directly to the console.

## 🛠️ Technologies Used
- **Language:** Python 3.x
- **Libraries:** Pandas, OpenPyXL
- **Data Source:** Excel (.xlsx) files

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/fazliozkul/bom-data-validator.git](https://github.com/fazliozkul/bom-data-validator.git)
---Install the required library:
pip install pandas openpyxl

---Run the script (it will generate a dummy Excel file and validate it):
python validator.py

--This script represents a simplified version of the automation logic I implemented to manage operational data flows, reducing manual verification time by approximately 40%.
