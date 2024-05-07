import csv
import os

def menu():
    ''' This function prints out a menu for the main program and gets user input,
    the user input is then returned for use in the main program '''
    
    print("Sales Records Management System\n")
    print("Please select an option below to get started")
    print("1. Load Customer and Sales Records")
    print("2. Save Customer Records")
    print("3. Save Sales Records")
    print("4. Quit Program")
    user_input = input("Type the number corresponding to your desired action: ")
    
    return user_input

def load_records():
    customers = {}
    sales = {}
                
    file1_name = input("\nplease provide the filename or filepath of customer records:")
    file2_name = input("please provide the filename or filepath of Sales record:")

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
    
    return customers, sales

def option1(dictionary):
        
    if not dictionary:  
        (customers, sales) = load_records()
        
        dictionary['customer_records'] = customers
        dictionary['sales_records'] = sales 
        
        
    else:
        overwrite = input("\nThe Data Structure holds record currently, do you want to overwrite [Y/N]")
        if overwrite.upper() == "Y" or overwrite == "":
            (customers, sales) = load_records()
            
            dictionary['customer_records'] = customers
            dictionary['sales_records'] = sales
            
        else:
            print(dictionary)
    
    return dictionary

