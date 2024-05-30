def option9(Loaded_records):
    ''' This function helps us delete a sales record by using it's transaction id. '''
    
    print("\nDelete sales record")
    
    record = "sales_records"
    sales_data = Loaded_records.get(record, {})
    
    trans_ids = []
    for key, value in sales_data.items():
        trans_ids.append(key)

    while True:
        trans_id = input("\nPlease enter transaction id* or 'stop' to quit: ")
        if trans_id != "":
            if trans_id in trans_ids:
                print(f"\n{Loaded_records[record][trans_id]}\nTransaction deleted")  
                del Loaded_records[record][trans_id]
                                        
            else:
                print("No transactions found")
                
        if trans_id.lower() == "stop":
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

option9(loaded_records)