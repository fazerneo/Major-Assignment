def option6(Loaded_records):
    
    search_string = input("\nPlease enter a search string: ")
    search_string = search_string.lower()
    
    
    for key, value in Loaded_records.items():
        if key == 'customer_records':
            for innerkey, innerval in Loaded_records.items():
                if (search_string in innerval['cust_id'] or 
                    search_string in innerval["name"].lower() or 
                    search_string in innerval["postcode"] or 
                    search_string in innerval["phone number"]):
                        print(innerkey, innerval)
            
        


Loaded_records = {'customer_records': {
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
        'phone number': '048531388'},
    '100002': {
        'cust_id': '100001', 
        'name': 'Brian Dombrowski', 
        'postcode': '6195', 
        'phone number': '048531388'}
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
option6(Loaded_records)