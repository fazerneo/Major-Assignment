import os

filename = "customers.csv"

# Check if the file exists in the current directory
if os.path.isfile(filename):
    print(f"The file '{filename}' exists in the current directory.")
else:
    print(f"The file '{filename}' does not exist in the current directory.")
