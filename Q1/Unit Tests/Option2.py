# This is an integration test for option2, save_records and Csv_writer because they are interdependent
# They were built initially into one function but seperated for efficient code

import os
import csv

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

def csv_writer(filepath, data, header):
    ''' This function is specifically made to be used by the save records function. It does the
    actual writing to the csv files while save records just works through the many possibilities. '''
    
    with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        row = []
        for value in data.values():
            for innervalue in value.values():
                row.append(innervalue)
            writer.writerow(row)
            row = []

def save_records(Loaded_records, record, header):
    ''' This function helps us save records to files. It takes 3 parameters, the dicionary, record,
    which according to chosen option in main program can be customer records or sales record and
    header according to the record. This function can be run by option 2 or option 3 in main program.
    It checks whether file exists or not in both windows and unix like devices, asks for permission to 
    overwrite if file exists or writes directly if file doesnt exist. It can accept both filename or filepath.
    It uses generalisation so that it can be called by both option 2 and 3 and deliver results accordingly.
    Note: if not dict is checked in function option2()'''
        
    data = Loaded_records.get(record, {})
    
    filepath = input(f"\nplease provide a filepath or filename where you want to save {record}: ")
    current_dir = os.getcwd()
    if "/" not in filepath or "\\" not in filepath:
        if "/" in current_dir:   
            filepath = current_dir + "/" + filepath
            if os.path.exists(filepath):
                overwrite = input("\nThe file already exists, do you want to overwrite [Y/N]")
                if overwrite.upper() == "Y" or overwrite == "":
                    csv_writer(filepath, data, header)
                    print("\nwrite complete")           
                                    
                else:
                    print("ok")
                    
            else:
                csv_writer(filepath, data, header)
                print("\nwrite complete")
                                    
        elif "\\" in current_dir:   
            filepath = current_dir + "\\" + filepath
            if os.path.exists(filepath):
                overwrite = input("\nThe file already exists, do you want to overwrite [Y/N]")
                if overwrite.upper() == "Y" or overwrite == "":
                    csv_writer(filepath, data, header)
                    print("\nwrite complete")
                                    
                else:
                    print("ok")
            else:
                csv_writer(filepath, data, header)
                print("\nwrite complete")  
                                    
    else:
        if os.path.exists(filepath):
            overwrite = input("\nThe file already exists, do you want to overwrite [Y/N]")
            if overwrite.upper() == "Y" or overwrite == "":
                csv_writer(filepath, data, header)
                print("\nwrite complete")
                    
            else:
                print("ok")

    return

loaded_records = {
    "customer_records": {
        "100000": {"cust_id": "100000", "name": "Christine Salt", "postcode": "6180", "phone number": "043908827"},
        "100001": {"cust_id": "100001", "name": "Brian Dombrowski", "postcode": "6132", "phone number": "048531388"},
        "100002": {"cust_id": "100002", "name": "Alan Manlio", "postcode": "6132", "phone number": "041949472"}
    },
    "sales_records": {
        "100000000": {"date": "2020-01-01", "customer_id": "100001", "category": "computer equipment", "value": 1144.16},
        "100000001": {"date": "2020-03-02", "customer_id": "100002", "category": "furniture", "value": 930.29},
        "100000002": {"date": "2020-01-03", "customer_id": "100002", "category": "household appliances", "value": 4520.66},
        "100000006": {"date": "2020-01-03", "customer_id": "100002", "category": "household appliances", "value": 4520.66},
        "100000007": {"date": "2020-04-03", "customer_id": "100002", "category": "alcohol and beverage", "value": 3577.84},
        "100000004": {"date": "2020-04-03", "customer_id": "100002", "category": "alcohol and beverage", "value": 3577.84},
        "100000011": {"date": "2020-04-03", "customer_id": "100002", "category": "alcohol and beverage", "value": 3577.84}
    }
}

option2(loaded_records)