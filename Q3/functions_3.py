import csv
import os
import numpy as np
import matplotlib.pyplot as plt

def menu():
    ''' This function prints out a menu for the main program and gets user input,
    the user input is then returned for use in the main program '''
    
    while True:
        try:
            print()
            print("Sales Records Management System\n")
            print("Please select an option below to get started")
            print("[1]. Load Customer and Sales Records    [8]. Display a customer's sales records")
            print("[2]. Save Customer Records              [9]. Delete a sales record")
            print("[3]. Save Sales Records                 [10]. Delete a customer")
            print("[4]. Add customer details               [11]. View monthly sales")
            print("[5]. Add sales details                  [12]. View monthly sales from a customer")
            print("[6]. Search customer details            [13]. View monthly sales from a postcode")
            print("[7]. search sales details               [14]. Quit Program")
            user_input = int(input("Type the number corresponding to your desired action: "))
            break
        except ValueError:
            print("Please enter a valid option between 1 and 14")
    
    return user_input

def option11(loaded_records):
    """ This function takes loaded_records as it's parameter, notes monthly sales using an ndarray 
    to store data according to month and plots a line graph to visualize """

    sales_data = loaded_records.get("sales_records", {})

    if not sales_data:
        print("\nThere are no sales records to view.")

    monthly_sales = np.zeros(12) 
    
    for value in sales_data.values():
        month = int(value['date'].split("-")[1])-1
        sales = float(value['value'])
        
        monthly_sales[month] += sales
    
    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    x = np.arange(1, 13)
    
    plt.figure(figsize=(10, 8))
    plt.plot(x, monthly_sales, marker='o')
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Monthly Sales")
    plt.xticks(x, Months)
    
    sales_max = monthly_sales.max()
    if sales_max != 0:
        step = round(sales_max * 0.1, -3)  
        if step == 0:
            step = round(sales_max * 0.1)  

    else:
        step = 1000  
    plt.yticks(np.arange(0, sales_max + step, step))
    plt.show()

def option12(loaded_records):
    """ This function takes loaded_records as it's parameter, notes monthly sales and number of sales
    using an ndarray to store data according to month and plots a two line graph on one axis
    to visualize monthly sales value of the customer and number of sales of the customer. """
    
    print("\nCustomer Sales Overview")
    customer_ids = []
    customer_data = loaded_records.get("customer_records", {})
    [customer_ids.append(value['cust_id']) for value in customer_data.values()]
    
    sales_data = loaded_records.get("sales_records", {})

    monthly_sales = np.zeros(12) 
    number_sales = np.zeros(12)
    
    plot = False
    customer_id = input("\nPlease enter customer's id: ")
    
    if customer_id != "":
        if customer_id in customer_ids:
            for value in sales_data.values():
                if customer_id in value["customer_id"]:
                    plot = True
                    month = int(value['date'].split("-")[1]) - 1
                    sales = float(value['value'])
                    
                    monthly_sales[month] += sales
                    number_sales[month] += 1
        
            if plot:       
                Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                x = np.arange(1, 13)
                
                fig, ax1 = plt.subplots(figsize=(12, 12))
                                
                plot1 = ax1.plot(x, monthly_sales, 'go-', label="Monthly Sales")

                ax1.set_xlabel("Month")
                ax1.set_ylabel("Sales")
                sales_max = monthly_sales.max()
    
                if sales_max != 0:
                    step = round(sales_max * 0.1, -3)  
                    if step == 0:
                        step = round(sales_max * 0.1)  

                else:
                    step = 1000  
                ax1.set_yticks(np.arange(0, sales_max + step, step))
                plt.title(f"Monthly Sales and Number of Sales for Customer {customer_id}")
                plt.xticks(x, Months)

                ax2 = ax1.twinx()
                
                plot2 = ax2.plot(x, number_sales,'b*--', label="Number of Sales", )
                ax2.set_yticks(number_sales+1)
                ax2.set_ylabel("Number of sales")
                
                lines1, labels1 = ax1.get_legend_handles_labels()
                lines2, labels2 = ax2.get_legend_handles_labels()
                plt.legend(lines1 + lines2, labels1 + labels2, loc='best')
                plt.show()        
            
            else:
                print("No customer transactions found")
            
        else:
            print("Customer ID does not exist")
    
    else:
        print("Error: Customer id should not be blank")

def option13(loaded_records):
    """ This function takes loaded_records as it's parameter, notes monthly sales and number of sales
    using an ndarray to store data according to month and plots a two line graph on one axis
    to visualize monthly sales value and number of sales of all the customers in a given postcode. """
    
    print("\nPostCode Sales Overview")
    postcodes = []
    customer_data = loaded_records.get("customer_records", {})
    [postcodes.append(value['postcode']) for value in customer_data.values()]
    
    sales_data = loaded_records.get("sales_records", {})

    monthly_sales = np.zeros(12) 
    number_sales = np.zeros(12)
    
    customers_in_postcode = []
    
    plot = False
    postcode = input("\nPlease enter postcode: ")
    if postcodes != "":
        if postcode in postcodes:
            customers_in_postcode = [value["cust_id"] for value in customer_data.values() if value['postcode'] == postcode]
            filtered_sales = [value for value in sales_data.values() if value["customer_id"] in customers_in_postcode]
            
            for value in filtered_sales:
                
                plot = True
                month = int(value['date'].split("-")[1]) - 1
                sales = float(value['value'])
                monthly_sales[month] += sales
                number_sales[month] += 1
        
            if plot:       
                Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                x = np.arange(1, 13)
                
                fig, ax1 = plt.subplots(figsize=(12, 12))
                                
                plot1 = ax1.plot(x, monthly_sales, 'go-', label="Monthly Sales")

                ax1.set_xlabel("Month")
                ax1.set_ylabel("Sales")

                ax1.set_yticks(monthly_sales) # make each step an average of last step. also edit option 12
                plt.title(f"Monthly Sales and Number of Sales for Postcode {postcode}")
                plt.xticks(x, Months)
                sales_max = monthly_sales.max()
    
                if sales_max != 0:
                    step = round(sales_max * 0.1, -3)  
                    if step == 0:
                        step = round(sales_max * 0.1)  

                else:
                    step = 1000  
                ax1.set_yticks(np.arange(0, sales_max + step, step))

                ax2 = ax1.twinx()
                
                plot2 = ax2.plot(x, number_sales,'b*--', label="Number of Sales", )
                
                ax2.set_yticks(np.arange(0, number_sales.max() + 2))
                ax2.set_ylabel("Number of sales")
                
                lines1, labels1 = ax1.get_legend_handles_labels()
                lines2, labels2 = ax2.get_legend_handles_labels()
                plt.legend(lines1 + lines2, labels1 + labels2, loc='best')
                
                plt.show()        
            
            else:
                print("No customer transactions found for the postcode")
            
        else:
            print("Postcode does not exist")
    
    else:
        print("Error: postcode should not be blank") 