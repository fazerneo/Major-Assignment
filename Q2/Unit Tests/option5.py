def option5(Loaded_records):
    ''' This function helps us add a new transaction, the user must give a customer id to whom the
    transaction belongs. if the customer exists, a new transaction detail can be added and it gets a
    unique autogenerated transaction id '''
    
    print("Add new transaction")
    
    customer_data = Loaded_records.get("customer_records", {})
    sales_data = Loaded_records.get("sales_records", {})
    
    customer_ids = []
    [customer_ids.append(key) for key in customer_data.keys()]
    
    while True:
        customer_id = input("\nPlease enter customer's id* or 'stop' to quit: ")
        if customer_id != "":
            if customer_id in customer_ids:
                date = input("Please enter the date of transaction (YYYY-MM-DD): ")
                category = input("Please enter the category of purchase: ")
                trans_value = input("Please enter the value of purchase: ")
                break
    
    trans_ids = []
    [trans_ids.append(int(key)) for key in sales_data.keys()]
        
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
    
    for key, value in sales_data.items():
        if key == trans_id:
            print(key, value)
            break
    
    print("New transaction added")
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

option5(loaded_records)
print(loaded_records)