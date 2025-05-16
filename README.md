# Automated Data QC Project

This project automates data quality checks on incoming CSV files.

## Overview

- The script scans the `incoming_data` folder for CSV files.
- It performs checks for missing values, duplicate rows, and expected column schema.
- Issues found are logged in `data_qc_log.txt`.
- A shell script `run_qc.sh` runs the checks and displays the latest log entries.

## How to Use

1. Place your CSV files in the `incoming_data` folder.
2. Activate your Python virtual environment:

   ```bash
   source myenv/Scripts/activate


### Run the data quality checks:

Run this: ./run_qc.sh

### Check the output on the terminal and review detailed logs in 

Run this: data_qc_log.txt


### Dependencies

- Python 3.x
- pandas library

### Install dependencies with:

Run this: pip install pandas