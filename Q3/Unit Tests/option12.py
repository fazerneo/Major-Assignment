import numpy as np
import matplotlib.pyplot as plt

def option12(loaded_records):
    """ This function takes loaded_records as it's parameter, notes monthly sales and number of sales
    using an ndarray to store data according to month and plots a two line graph on one axis
    to visualize monthly sales value of the customer and number of sales of the customer. """
    
    print("\nCustomer Sales Overview")
    customer_ids = []
    customer_data = loaded_records.get("customer_records", {})
    print(customer_data)
    
    [customer_ids.append(value['cust_id']) for value in customer_data.values()]
    
    sales_data = loaded_records.get("sales_records", {})

    monthly_sales = np.zeros(12) 
    number_sales = np.zeros(12)
    
    plot = False
    customer_id = "100001" #try 100001
    if customer_id != "":
        if customer_id in customer_ids:
            for value in sales_data.values():
                if customer_id in value["customer_id"]:
                    plot = True
                    month = int(value['date'].split("-")[1]) - 1
                    sales = value['value']
                    
                    monthly_sales[month] += sales
                    number_sales[month] += 1
                    print(monthly_sales)
        
            if plot:       
                Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                x = np.arange(1, 13)
                
                fig, ax1 = plt.subplots(figsize=(12, 12))
                                
                plot1 = ax1.plot(x, monthly_sales, 'go-', label="Monthly Sales")

                ax1.set_xlabel("Month")
                ax1.set_ylabel("Sales")
                sales_max = monthly_sales.max()
                step = round(sales_max * 0.1, -3)
    
                ax1.set_yticks(np.arange(0, sales_max + step, step))
                plt.title(f"Monthly Sales and Number of Sales for Customer {customer_id}")
                plt.xticks(x, Months)

                ax2 = ax1.twinx()
                
                plot2 = ax2.plot(x, number_sales,'b*--', label="Number of Sales", )
                ax2.set_yticks(number_sales+1)
                ax2.set_ylabel("Number of sales")
                
                lines1, labels1 = ax1.get_legend_handles_labels()
                lines2, labels2 = ax2.get_legend_handles_labels()
                plt.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
                plt.show()        
            
            else:
                print("No customer transactions found")
            
        else:
            print("Customer ID does not exist")
    
    else:
        print("Error: Customer id should not be blank")
    


    
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

option12(loaded_records)