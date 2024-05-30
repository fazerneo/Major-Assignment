def option6(Loaded_records):
    ''' This function helps us search through customer records using a case-insensitive string.
    The search is made across customer id, name, postcode and phone number '''
    
    print("\nSearch customer records")
    customer_data = Loaded_records.get("customer_records", {})
    
    while True:
        search_string = input("\nPlease enter a search string or 'stop' to quit: ").lower()
        matches = {}
        for key, value in customer_data.items():
            if (search_string in value['cust_id'] or
                search_string in value['name'].lower() or
                search_string in value['postcode'] or
                search_string in value['phone number']):
                
                matches[key] = value
        
        if matches:
            for key, value in matches.items():
                print(key, value)
        else:
            print("no records found")
            
        if search_string == "stop":
            break
    
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

option6(loaded_records)