import os ### Accessing file system
import pandas as pd ### To read and validate the data
from datetime import datetime ### Timestamp the log entries
print("Python script is running")  ### Confirm the Python script is being executed


# Define folder to scan and log file location
DATA_FOLDER = "incoming_data"  ### New Data gets dropped in.
LOG_FILE = "data_qc_log.txt"   ### Tracking what the script finds.

# Get all CSV files in the data folder
csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.csv')]

# If no files found, log and exit
if not csv_files:
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] No CSV files found in '{DATA_FOLDER}'.\n")
    exit()

# Loop through each CSV file and perform checks
for file in csv_files:
    file_path = os.path.join(DATA_FOLDER, file)
    df = pd.read_csv(file_path)

    issues = []

    # Check for missing values
    if df.isnull().values.any():
        issues.append("Missing values detected")

    # Check for duplicate rows
    if df.duplicated().any():
        issues.append("Duplicate rows found")

    # Define expected columns and check schema; expect to see in every data file.
    expected_columns = ['id', 'name', 'date', 'value']
    if list(df.columns) != expected_columns:
        issues.append("Unexpected column schema")

    # Log the results
    with open(LOG_FILE, 'a') as log:
        if issues:
            log.write(f"[{datetime.now()}] Issues in '{file}': {', '.join(issues)}\n")
        else:
            log.write(f"[{datetime.now()}] '{file}' passed all quality checks.\n")
