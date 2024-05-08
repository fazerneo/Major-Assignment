import os
import csv

filepath = "staff.csv"
header = ['cust_id','name','postcode','phone number']
record = 'customer records'

dictionary = {
    'customer records': {
        '1001': {
            'cust_id': '1001',
            'name': 'Alice',
            'postcode': '12345',
            'phone number': '555-1234'
        },
        '1002': {
            'cust_id': '1002',
            'name': 'Bob',
            'postcode': '23456',
            'phone number': '555-5678'
        },
        '1003': {
            'cust_id': '1003',
            'name': 'Charlie',
            'postcode': '34567',
            'phone number': '555-7890'
        }
    },
    'sales record': {
        '2001': {
            'cust_id': '1001',
            'name': 'Sale1',
            'postcode': '12345',
            'phone number': '555-1111'
        },
        '2002': {
            'cust_id': '1002',
            'name': 'Sale2',
            'postcode': '23456',
            'phone number': '555-2222'
        },
        '2003': {
            'cust_id': '1003',
            'name': 'Sale3',
            'postcode': '34567',
            'phone number': '555-3333'
        }
    }
}

with open(filepath, "w+", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    row = []
    for key, value in dictionary.items():
        if key == record:
            for innerkey, innerval in value.items():
                for deepkey, deepval in innerval.items():
                    row.append(deepval)
                writer.writerow(row)
                row = []
                


