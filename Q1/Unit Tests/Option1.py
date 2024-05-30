# This is an integration test for option1, load_records and print_dict. Option1 is dependent on load_records
# print_dict is just a function like the command line head tool for users comfort

import os
import csv

def option1(dictionary):
    ''' This function takes a dictionary as the parameter. If the dictionary is empty, it loads customer
    and sales records from another function, these are sent to the dictionary. If the dictionary is not
    empty due to loads from option1 or saves from other options, it asks user for overwrite permission.
    If overwrite access is given, the load_records function is called and customer and sales records are
    sent to the dictionary. If overwrite function is not given, then the function just prints the dictionary 
    and returns the dictionary for any further use. '''
    
    print("\nLoad csv files")
    
    if not dictionary: # evaluates to True if dictionary is empty. now we have an empty dictionary to work on
        (customers, sales) = load_records() # call a function and save into variables.
        dictionary['customer_records'] = customers # update dictionary with key
        dictionary['sales_records'] = sales 

    else: # if dicionary is not empty
        overwrite = input("\nThe Data Structure holds record currently, do you want to overwrite [Y/N]")
        if overwrite.upper() == "Y" or overwrite == "": # if overwrite access is y, Y or just enter
            (customers, sales) = load_records()
            dictionary['customer_records'] = customers
            dictionary['sales_records'] = sales
        else:
            print()
            print("Records")
            print(dictionary)
    
    return dictionary

def load_records():
    ''' This is definitely a long function but I couldnt do it any shorter without creating more functions.
    This function initializes two dictionaries, gets file names as input, checks for whether the file exists,
    if the file does not exist then it asks for new file names, then the records in the files are iterated over
    and sent to dictionaries. This function returns the filled dictionaries. '''
    
    customers = {}
    sales = {}

    file1_name = "Q1/Q1 test data/customers.csv"
    
    while True:
        
        if "/" not in file1_name or "\\" not in file1_name: # if user enters filename instead of path
            current_dir = os.getcwd()
            if "/" in current_dir: # if users are using Linux, Mac or other unix like OS
                file1_name = current_dir + "/" + file1_name
                if os.path.exists(file1_name):
                    break
                else:
                    print("\nThe customer records filename or filepath you provided is not valid")
                    file1_name = input("\nplease provide a valid filename or filepath: ")
            elif "\\" in current_dir: # if users are using windows
                file1_name = current_dir + "\\" + file1_name
                if os.path.exists(file1_name):
                    break
                else:
                    print("\nThe customers record filename or filepath you provided is not valid")

                    file1_name = input("\nplease provide a valid filename or filepath: ")   
        
        else: # if user enters path instead of filename
            if os.path.exists(file1_name):
                break
            else:
                print("\nThe customers record filename or filepath you provided is not valid")
                file1_name = input("\nplease provide a valid filename or filepath: ")

    file2_name = "Q1/Q1 test data/sales.csv"    
    
    while True:
        
        if "/" not in file2_name or "\\" not in file2_name:
            current_dir = os.getcwd()
            if "/" in current_dir:
                file2_name = current_dir + "/" + file2_name
                if os.path.exists(file2_name):
                    break
                else:
                    print("\nThe sales record filename or filepath you provided is not valid")
                    file2_name = input("\nplease provide a valid filename or filepath: ")
            elif "\\" in current_dir:
                file2_name = current_dir + "\\" + file2_name
                if os.path.exists(file2_name):
                    break
                else:
                    print("\nThe sales record filename or filepath you provided is not valid")
                    file2_name = input("\nplease provide a valid filename or filepath: ")
            
        else:
            if os.path.exists(file2_name):
                break
            else:
                print("\nThe sales record filename or filepath you provided is not valid")
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
    
    return customers, sales

def print_dict(dictionary, num_lines):
    ''' This function takes a dictionary and num_lines as its parameter and prints the records line by line.
    num_lines acts like head command and tha number of records is printed. '''
    
    count = num_lines # I set a count here to act like head
    count = int(count)
    
    print()
    print("Loaded Records")
    
    if count != "" or count > 0:
        for key, value in dictionary.items(): # this iterates over entries in the dictionary('customer records' and 'sales record')
            print()
            print(key)
            
            for inner_key, inner_value in value.items(): # this iterates over the inner dictionaries
                print(inner_value)
                count -= 1
                
                if count == 0:# if count has become zero, it is reset to num_lines so that second record also gets same treatment as record 1
                    count = num_lines
                    count = int(count)
                    break
        print("\nLoad Complete")


dictionary = {}      
option1(dictionary)
print_dict(dictionary, "2")