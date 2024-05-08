import csv
import os

customers = {}
sales = {}

file1_name = input("\nplease provide the filename or filepath of customer records:")
while True:
    path = file1_name
    if "/" not in file1_name or "\\" not in file1_name:
        current_dir = os.getcwd()
        if "/" in current_dir:
            path = current_dir + "/" + path
            if os.path.exists(path):
                break
            else:
                print("\nThe customer records filename or filepath you provided is not valid")
                print("Examples of valid filenames or filepaths: \"customers.csv\" or \"Q1 tests/customers.csv\"")
                file1_name = input("\nplease provide a valid filename or filepath: ")
        elif "\\" in current_dir:
            path = current_dir + "\\" + path
            if os.path.exists(path):
                break
            else:
                print("\nThe customers record filename or filepath you provided is not valid")
                print("Examples of valid filenames or filepaths: \"customers.csv\" or \"Q1 tests/customers.csv\"")
                file1_name = input("\nplease provide a valid filename or filepath: ")   
    else:
        if os.path.exists(path):
            break
        else:
            print("\nThe customers record filename or filepath you provided is not valid")
            print("Examples of valid filenames or filepaths: \"customers.csv\" or \"Q1 tests/customers.csv\"")
            file1_name = input("\nplease provide a valid filename or filepath: ")

file2_name = input("please provide the filename or filepath of Sales record:")    
while True:
    path = file2_name
    if "/" not in file2_name or "\\" not in file2_name:
        current_dir = os.getcwd()
        if "/" in current_dir:
            path = current_dir + "/" + path
            if os.path.exists(path):
                break
            else:
                print("\nThe sales record filename or filepath you provided is not valid")
                print("Examples of valid filenames or filepaths: \"sales.csv\" or \"Q1 tests/sales.csv\"")
                file2_name = input("\nplease provide a valid filename or filepath: ")
        elif "\\" in current_dir:
            path = current_dir + "\\" + path
            if os.path.exists(path):
                break
            else:
                print("\nThe sales recordfilename or filepath you provided is not valid")
                print("Examples of valid filenames or filepaths: \"sales.csv\" or \"Q1 tests/sales.csv\"")
                file2_name = input("\nplease provide a valid filename or filepath: ")
        
    else:
        if os.path.exists(path):
            break
        else:
            print("\nThe filename or filepath you provided is not valid")
            print("Examples of valid filenames or filepaths: \"sales.csv\" or \"Q1 tests/sales.csv\"")
            file2_name = input("\nplease provide a valid filename or filepath: ")
    
    
with open(file1_name, newline="", encoding="utf-8-sig") as file1, open(file2_name, newline="", encoding="utf-8-sig") as file2:
    reader1 = csv.DictReader(file1)
    reader2 = csv.DictReader(file2) 
                
    for row in reader1:
        customers[row["cust_id"]] = {
            "cust_id": row["cust_id"],
            "name": row["name"],
            "postcode": row["postcode"],
            "phone number": row["phone number"]
        }
                
                
    for row in reader2:
        sales[row["trans_id"]] = {
            "date": row["date"],
            "trans_id": row["trans_id"],
            "customer_id": row["customer_id"],
            "category": row["category"],
            "value": row["value"]
        }
                
print(customers)
print(sales)