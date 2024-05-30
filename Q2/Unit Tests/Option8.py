def option8(Loaded_records):
    ''' This function helps us search for all transactions a customer has made using their customer id.
    if the customer id exists, all related transactions are listed. '''
    
    print("\nsales records from a customer using his/her customer id.")
    customer_data = Loaded_records.get("customer_records", {})
    sales_data = Loaded_records.get("sales_records", {})
    customer_ids = []
    [customer_ids.append(key) for key in customer_data.keys()]
    
    while True:
        customer_id = input("\nPlease enter customer's id* or 'stop' to quit: ")
        if customer_id != "":
            if customer_id in customer_ids:
                matches = {}
                for key, value in sales_data.items():
                    if customer_id in value["customer_id"]:
                        matches[key] = value
                
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

option8(loaded_records)