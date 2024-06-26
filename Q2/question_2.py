from functions_1 import *
from functions_2 import *

# empty global dictionary
Loaded_records = {}

while True: 
    user_input = menu()
    
    # if user input is 1, to load records, option1 func is called with the empty global dict as param
    # the loaded dict is passed to the global dict
    # a head like function is passed to only print a few number of lines to not overload console
    if user_input == 1:
        Loaded_records = option1(Loaded_records)
        head = int(input("\nEnter the number of records you want to print for each record.\nThis will ensure large data records dont overload our console: "))
        print_dict(Loaded_records, head)
    
    # if user input is 2, option2 func is passed with the global dict
    # only the customer records is saved to a desired filename or filepath
    elif user_input == 2:
        option2(Loaded_records)
    
    # only the sales records is saved to a desired filename or filepath
    elif user_input == 3:
        option3(Loaded_records)
    
    # if user input is 4, option 4 is passed with global dictionary and the mutated dictionary is returned
    # A new customer is added with unique autogenerated cust_id
    elif user_input == 4:
        Loaded_records = option4(Loaded_records)
    
    # A new transaction is created with unique autogenerated transaction id
    elif user_input == 5:
        Loaded_records = option5(Loaded_records)
    
    # we can search for customer records using any character that might be in the specific records
    elif user_input == 6:
        option6(Loaded_records)
    
    # we can search for transaction records using anything that may appear in the record's data, category, value or transaction id
    elif user_input == 7:
        option7(Loaded_records)
        
    # we can search for a customer's transactions using his/her customer id
    elif user_input == 8:
        option8(Loaded_records)
    
    # we can delete a transaction using its transaction id   
    elif user_input == 9:
        Loaded_records = option9(Loaded_records)
    
    # we can delete a customer using his/her customer id. This also deletes all of his/her transactions  
    elif user_input == 10:  
        Loaded_records = option10(Loaded_records)
    
    # if user input is 11, we exit the looping menu
    elif user_input == 11:
        print("\nThank you for using the program")
        break
        