from functions import *

Loaded_records = {}

while True: 
    
    user_input = menu()
    
    if user_input == 1:
        Loaded_records = option1(Loaded_records)
        head = input("\nEnter the number of records you want to print for each record.\nThis will ensure large data records dont overload our console: ")
        print_dict(Loaded_records, head)
    
    elif user_input == 2:
        option2(Loaded_records)
        
    elif user_input == 3:
        option3(Loaded_records)
    
    elif user_input == 4:
        print("\nThank you for using the program")
        break
        