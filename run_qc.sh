#!/bin/bash

# Print start message
echo "Running data quality checks..."

# Activate the virtual environment
source myenv/Scripts/activate

# Run the Python script
python data_qc_checker.py

# Print completion message
echo "Data quality check complete."
