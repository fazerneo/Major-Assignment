from functions_1 import *

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
    
    # if user input is 3, option3 func is passed with the global dict
    # only the sales records is saved to a desired filename or filepath
    elif user_input == 3:
        option3(Loaded_records)
    
    # if user input is 4, we exit the looping menu
    elif user_input == 4:
        print("\nThank you for using the program")
        break
        