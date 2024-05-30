
def option10(Loaded_records):
    ''' This function helps us delete a customer using his/her customer id. It also deletes all of his/her
    transactions. '''
    
    print("\nDelete customer and related transactions")
    
    record = "customer_records"
    customer_data = Loaded_records.get(record, {})
    sales_data = Loaded_records.get("sales_records", {})
    print(sales_data)
    
    cust_ids = []
    [cust_ids.append(value['cust_id']) for value in customer_data.values()]
    
    while True:
        cust_id = input("\nPlease enter customer id* or 'stop' to quit: ")
        if cust_id != "":
            if cust_id in cust_ids:
                print(f"\n{Loaded_records[record][cust_id]}\ncustomer deleted")  
                del Loaded_records[record][cust_id]
                        
                trans_to_delete = []
                for key, value in sales_data.items():
                    if cust_id == value['customer_id']:
                        trans_to_delete.append(key)
                
                for i in trans_to_delete:
                    print(f"\n{Loaded_records['sales_records'][i]}\ntransaction deleted")  
                    del Loaded_records['sales_records'][i]             

            else:
                print("No customer found")
                
        if cust_id.lower() == "stop":
            break
        
    return Loaded_records

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

option10(loaded_records)
print(loaded_records)