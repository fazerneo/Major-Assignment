import csv
import os

def menu():
    ''' This function prints out a menu for the main program and gets user input,
    the user input is then returned for use in the main program '''
    
    while True:
        try:
            print()
            print("Sales Records Management System\n")
            print("Please select an option below to get started")
            print("[1]. Load Customer and Sales Records")
            print("[2]. Save Customer Records")
            print("[3]. Save Sales Records")
            print("[4]. Add customer details")
            print("[5]. Add sales details")
            print("[6]. Search customer details")
            print("[7]. search sales details")
            print("[8]. Display a customer's sales records")
            print("[9]. Delete a sales record")
            print("[10]. Delete a customer")
            print("[11]. Quit Program")
            user_input = int(input("Type the number corresponding to your desired action: "))
            break
        except ValueError:
            print("Please enter a valid option between 1 and 4")
    
    return user_input

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

def option2(Loaded_records):
    ''' This option simply initializes record, header and checks whether the dictionary in memory is
    populated or not. if it is empty, it shows a message to the user, if it is populated, it calls the
    general save records function which either it or option3 can use. '''
    
    print("\nSave customer records")
    
    record = 'customer_records'
    header = ['cust_id','name','postcode','phone number']
    
    if not Loaded_records:
        print("\nThere are no records to be written yet. Please load some records to get started.")
    else:
        dictionary = Loaded_records.copy()
        save_records(dictionary, record, header)
    
    return

def option3(Loaded_records):
    ''' This option simply initializes record, header and checks whether the dictionary in memory is
    populated or not. if it is empty, it shows a message to the user, if it is populated, it calls the
    general save records function which either it or option2 can use. '''
    
    print("\nSave sales records")
    
    record = 'sales_records'
    header = ['date','trans_id','customer_id','category','value']
    
    if not Loaded_records:
        print("\nThere are no records to be written yet. Please load some records to get started.")
    else:
        dictionary = Loaded_records.copy()
        save_records(dictionary, record, header)
    
    return

def option4(Loaded_records):
    
    print("\nAdd new customer")
    
    while True:
        name = input("\nPlease enter customer's name*: ")
        if name != "":
            break
    postcode = input("Please enter customer's postcode: ")
    phone_number = input("Please enter customer's phone number: ")
    
    record = 'customer_records'
    customer_ids = []
    for key, value in Loaded_records.items():
        if key == record:
            for innerkey, innerval in value.items():
                innerkey = int(innerkey)
                customer_ids.append(innerkey)
        
    cust_id = 0
    for i in range(100000, 999999):
        if i not in customer_ids:
            cust_id = i
            break
    
    cust_id = str(cust_id)    
        
    new_customer = {
            'cust_id': cust_id,
            'name': name,
            'postcode': postcode,
            'phone number': phone_number
        }
    
    Loaded_records['customer_records'][cust_id] = new_customer
    
    print()
    
    for key, value in Loaded_records.items():
        if key == record:
            for innerkey, innerval in value.items():
                if innerkey == cust_id:
                    print(innerkey, innerval)
                    break
    
    print("New customer added")
    return Loaded_records

def option5(Loaded_records):
    
    print("Add new transaction")
    
    record = "customer_records"
    customer_ids = []
    for key, value in Loaded_records.items():
        if key == record:
            for innerkey, innerval in value.items():
                customer_ids.append(innerkey)
    
    while True:
        customer_id = input("\nPlease enter customer's id*: ")
        if customer_id != "":
            if customer_id in customer_ids:
                date = input("Please enter the date of transaction: ")
                category = input("Please enter the category of purchase: ")
                trans_value = input("Please enter the value of purchase: ")
                break
            else:
                print("Customer id does not exist, please create a new id if it is a new customer.")
                user_input = input("Would you like to create a new customer id [Y/N]: ")
                if user_input.lower() == 'y':
                    Loaded_records = option4(Loaded_records)
                    break
    
    record = 'sales_records'
    trans_ids = []
    for key, value in Loaded_records.items():
        if key == record:
            for innerkey, innerval in value.items():
                innerkey = int(innerkey)
                trans_ids.append(innerkey)
        
    trans_id = 0
    for i in range(100000000, 999999999):
        if i not in trans_ids:
            trans_id = i
            break
    
    trans_id = str(trans_id)    
        
    new_trans = {
            "date": date,
            "trans_id": trans_id,
            "customer_id": customer_id,
            "category": category,
            "value": trans_value
        }
    
    Loaded_records['sales_records'][trans_id] = new_trans
    
    print()
    
    for key, value in Loaded_records.items():
        if key == record:
            for innerkey, innerval in value.items():
                if innerkey == trans_id:
                    print(innerkey, innerval)
                    break
    
    print("New transaction added")
    return Loaded_records

def option6(Loaded_records):
    
    print("\nSearch customer records")
    
    while True:
        search_string = input("\nPlease enter a search string: ").lower()
        matches = {}
        for key, value in Loaded_records.items():
            if key == 'customer_records':
                for innerkey, innerval in value.items():
                    if (search_string in innerval['cust_id'] or
                        search_string in innerval['name'].lower() or
                        search_string in innerval['postcode'] or
                        search_string in innerval['phone number']):
                        
                        matches[innerkey] = innerval
        
        if matches:
            for key, value in matches.items():
                print(key, value)
        else:
            print("no records found")
            
        if search_string == "stop":
            break
    
    return

def option7(Loaded_records):
    
    print("\nSearch sales records")
    
    while True:
        search_string = input("\nPlease enter a search string: ").lower()
        matches = {}
        for key, value in Loaded_records.items():
            if key == 'sales_records':
                for innerkey, innerval in value.items():
                    if (search_string in innerval['date'] or
                        search_string in innerval['customer_id'].lower() or
                        search_string in innerval['category'] or
                        search_string in innerval['value']):
                        
                        matches[innerkey] = innerval
        
        if matches:
            for key, value in matches.items():
                print(key, value)
        else:
            print("no records found")
            
        if search_string == "stop":
            break
        
    return

def option8(Loaded_records):
    print("\nsales records from a customer using his/her customer id.")
    record = "customer_records"
    customer_ids = []
    for key, value in Loaded_records.items():
        if key == record:
            for innerkey, innerval in value.items():
                customer_ids.append(innerkey)
    
    while True:
        customer_id = input("\nPlease enter customer's id*: ")
        if customer_id != "":
            if customer_id in customer_ids:
                matches = {}
                for key, value in Loaded_records.items():
                    if key == 'sales_records':
                        for innerkey, innerval in value.items():
                            if customer_id in innerval["customer_id"]:
                                
                                matches[innerkey] = innerval
                
                if matches:
                    num = 1
                    for key, value in matches.items():
                        print(f"{num}. {value}")
                        num += 1
                else:
                    print("No customer transactions found")
                
            else:
                print("Customer ID does not exist")

        if customer_id.lower() == "stop":
            break
        
    return

def option9(Loaded_records):
    pr

def load_records():
    ''' This is definitely a long function but I couldnt do it any shorter without creating more functions.
    This function initializes two dictionaries, gets file names as input, checks for whether the file exists,
    if the file does not exist then it asks for new file names, then the records in the files are iterated over
    and sent to dictionaries. This function returns the filled dictionaries. '''
    
    customers = {}
    sales = {}

    file1_name = input("\nplease provide the filename or filepath of customer records:")
    
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

    file2_name = input("please provide the filename or filepath of Sales record:")    
    
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
            
    elif count == "":
        for key, value in dictionary.items(): # this iterates over entries in the dictionary('customer records' and 'sales record')
            print()
            print(key)
            
            for inner_key, inner_value in value.items(): # this iterates over the inner dictionaries
                print(inner_value)
        print("\nLoad Complete")
            
    else:
        print("\nLoad Complete")
                    
    return

def save_records(Loaded_records, record, header):
    ''' This function helps us save records to files. It takes 3 parameters, the dicionary, record,
    which according to chosen option in main program can be customer records or sales record and
    header according to the record. This function can be run by option 2 or option 3 in main program.
    It checks whether file exists or not in both windows and unix like devices, asks for permission to 
    overwrite if file exists or writes directly if file doesnt exist. It can accept both filename or filepath.
    It uses generalisation so that it can be called by both option 2 and 3 and deliver results accordingly.
    Note: if not dict is checked in function option2()'''
    
    
    filepath = input(f"\nplease provide a filepath or filename where you want to save {record}: ")
    current_dir = os.getcwd()
    if "/" not in filepath or "\\" not in filepath:
        if "/" in current_dir:   
            filepath = current_dir + "/" + filepath
            if os.path.exists(filepath):
                overwrite = input("\nThe file already exists, do you want to overwrite [Y/N]")
                if overwrite.upper() == "Y" or overwrite == "":
                    with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
                        writer = csv.writer(file)
                        writer.writerow(header)
                        row = []
                        for key, value in Loaded_records.items():
                            if key == record:
                                for innerkey, innerval in value.items():
                                    for deepkey, deepval in innerval.items():
                                        row.append(deepval)
                                    writer.writerow(row)
                                    row = []
                        print("\nwrite complete")           
                                    
                else:
                    print("ok")
            else:
                with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
                        writer = csv.writer(file)
                        writer.writerow(header)
                        row = []
                        for key, value in Loaded_records.items():
                            if key == record:
                                for innerkey, innerval in value.items():
                                    for deepkey, deepval in innerval.items():
                                        row.append(deepval)
                                    writer.writerow(row)
                                    row = []
                        print("\nwrite complete")
                                    
        elif "\\" in current_dir:   
            filepath = current_dir + "\\" + filepath
            if os.path.exists(filepath):
                overwrite = input("\nThe file already exists, do you want to overwrite [Y/N]")
                if overwrite.upper() == "Y" or overwrite == "":
                    with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
                        writer = csv.writer(file)
                        writer.writerow(header)
                        row = []
                        for key, value in Loaded_records.items():
                            if key == record:
                                for innerkey, innerval in value.items():
                                    for deepkey, deepval in innerval.items():
                                        row.append(deepval)
                                writer.writerow(row)
                                row = []
                        print("\nwrite complete")
                                    
                else:
                    print("ok")
            else:
                with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
                        writer = csv.writer(file)
                        writer.writerow(header)
                        row = []
                        for key, value in Loaded_records.items():
                            if key == record:
                                for innerkey, innerval in value.items():
                                    for deepkey, deepval in innerval.items():
                                        row.append(deepval)
                                writer.writerow(row)
                                row = []
                        print("\nwrite complete")   
                                    
    else:
        if os.path.exists(filepath):
            overwrite = input("\nThe file already exists, do you want to overwrite [Y/N]")
            if overwrite.upper() == "Y" or overwrite == "":
                with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    row = []
                    for key, value in Loaded_records.items():
                        if key == record:
                            for innerkey, innerval in value.items():
                                for deepkey, deepval in innerval.items():
                                    row.append(deepval)
                            writer.writerow(row)
                            row = []
                    print("\nwrite complete")
                    
            else:
                print("ok")
        
    
    

    return

