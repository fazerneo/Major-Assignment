import os
import csv

def save_records(Loaded_records, record, header):
    ''' This function helps us save records to files. It takes 3 parameters, the dicionary, record,
    which according to chosen option in main program can be customer records or sales record and
    header according to the record. This function can be run by option 2 or option 3 in main program.
    It checks whether file exists or not in both windows and unix like devices, asks for permission to 
    overwrite if file exists or writes directly if file doesnt exist. It can accept both filename or filepath.
    It uses generalisation so that it can be called by both option 2 and 3 and deliver results accordingly.
    Note: if not dict is checked in function option2()'''
    print(Loaded_records)
    if Loaded_records:
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
        
    
    else:
        print("\nThere are no records to be written yet. Please load some records to get started.")

    return

def option2():
    ''' This option simply initializes record, header and checks whether the dictionary in memory is
    populated or not. if it is empty, it shows a message to the user, if it is populated, it calls the
    general save records function which either it or option3 can use. '''
    record = 'customer_records'
    header = ['cust_id','name','postcode','phone number']
    
    return record, header

def option3():
    ''' This option simply initializes record, header and checks whether the dictionary in memory is
    populated or not. if it is empty, it shows a message to the user, if it is populated, it calls the
    general save records function which either it or option2 can use. '''
    record = 'sales_records'
    header = ['date','trans_id','customer_id','category','value']
    
    return record, header

Loaded_records = {'customer_records': {'100000': {'cust_id': '100000', 'name': 'Christine Salt', 'postcode': '6180', 'phone number': '043908827'}, '100001': {'cust_id': '100001', 'name': 'Brian Dombrowski', 'postcode': '6195', 'phone number': '048531388'}, '100002': {'cust_id': '100002', 'name': 'Alan Manlio', 'postcode': '6132', 'phone number': '041949472'}, '100003': {'cust_id': '100003', 'name': 'Sarah Sands', 'postcode': '6218', 'phone number': '044076280'}}, 'sales_records': {'100000000': {'date': '2020-01-01', 'trans_id': '100000000', 'customer_id': '100060', 'category': 'computer equipment', 'value': '1144.16'}, '100000001': {'date': '2020-01-02', 'trans_id': '100000001', 'customer_id': '100061', 'category': 'furniture', 'value': '930.29'}, '100000002': {'date': '2020-01-03', 'trans_id': '100000002', 'customer_id': '100043', 'category': 'household appliances', 'value': '4520.66'}, '100000003': {'date': '2020-01-03', 'trans_id': '100000003', 'customer_id': '100039', 'category': 'alcohol and beverage', 'value': '3577.84'}, '100000004': {'date': '2020-01-03', 'trans_id': '100000004', 'customer_id': '100098', 'category': 'alcohol and beverage', 'value': '4279.75'}}}
(param2, param3) = option2()
save_records(Loaded_records, param2, param3)
(param2, param3) = option3()
save_records(Loaded_records, param2, param3)