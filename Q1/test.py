import csv

customers = {}
sales = {}
#file1_name = input("please provide the filename or filepath of customer records:")
#file2_name = input("please provide the filename or filepath of Sales record:")

with open("Q1 tests/customers.csv", newline="", encoding="utf-8-sig") as file1, open("Q1 tests/sales.csv", newline="", encoding="utf-8-sig") as file2:
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
    
    
    