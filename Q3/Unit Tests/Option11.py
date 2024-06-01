import numpy as np
import matplotlib.pyplot as plt

def option11(loaded_records):
    """ This function takes loaded_records as it's parameter, notes monthly sales using an ndarray 
    to store data according to month and plots a line graph to visualize """

    sales_data = loaded_records.get("sales_records", {})

    if not sales_data:
        print("\nThere are no sales records to view.")

    monthly_sales = np.zeros(12) 
    print(monthly_sales)
    for value in sales_data.values():
        month = int(value['date'].split("-")[1])-1
        sales = value['value']
        
        monthly_sales[month] += sales
        
    print(monthly_sales)
    
    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    x = np.arange(1, 13)
    
    plt.figure(figsize=(10, 8))
    plt.plot(x, monthly_sales, marker='o')
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales")
    
    sales_max = monthly_sales.max()
    step = round(sales_max * 0.1, -3)
    
    plt.yticks(np.arange(0, sales_max + step, step))
    plt.xticks(x, Months)
    plt.tight_layout()
    plt.show()


    
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
option11(loaded_records)