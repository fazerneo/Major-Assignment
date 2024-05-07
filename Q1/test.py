import csv

customers = {}
sales = {}
#file1_name = input("please provide the filename or filepath of customer records:")
#file2_name = input("please provide the filename or filepath of Sales record:")

with open("/Q1 tests/customers.csv") as file1:
    reader1 = csv.DictReader(file1)
    
    for row in reader1:
        print("yes")
        print(row['cust_id'])
    

with open("/Q1 tests/sales.csv") as file2:
    reader2 = csv.DictReader(file2)  
    for row in reader2:
        print(row["date"])   