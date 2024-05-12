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

# Example usage:
Loaded_records = {
    'customer_records': {
        '100000': {
            'cust_id': '100000', 
            'name': 'Christine Salt', 
            'postcode': '6180', 
            'phone number': '043908827'
        }, 
        '100001': {
            'cust_id': '100001', 
            'name': 'Brian Dombrowski', 
            'postcode': '6195', 
            'phone number': '048531388'
        },
        '100060': {
            'cust_id': '100002', 
            'name': 'John Smith', 
            'postcode': '6150', 
            'phone number': '0412345678'
        },
        '100061': {
            'cust_id': '100001', 
            'name': 'Brian wazowski', 
            'postcode': '6195', 
            'phone number': '048531388'
        },
    },
    'sales_records': {
        '100000000': {
            'date': '2020-01-01', 
            'trans_id': '100000000', 
            'customer_id': '100060', 
            'category': 'computer equipment', 
            'value': '1144.16'
        },
        '100000001': {
            'date': '2020-01-02', 
            'trans_id': '100000001', 
            'customer_id': '100061', 
            'category': 'furniture', 
            'value': '930.29'
        }
    }
}

option8(Loaded_records)
