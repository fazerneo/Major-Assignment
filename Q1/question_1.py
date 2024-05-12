from functions import *

Loaded_records = {}

while True: 
    
    user_input = menu()
    user_input = int(user_input)
    
    if user_input == 1:
        Loaded_records = option1(Loaded_records)
        print(Loaded_records)
        head = input("\nEnter the number of records you want to print for each record.\nThis will ensure large data records dont overload our console: ")
        print_dict(Loaded_records, head)
    
    elif user_input == 2:
        dictionary = Loaded_records.copy()
        (param2, param3) = option2()
        save_records(dictionary, param2, param3)
        
    elif user_input == 3:
        dictionary = Loaded_records.copy()
        (param2, param3) = option3()
        save_records(dictionary, param2, param3)
    
    elif user_input == 4:
        print("\nThank you for using the program")
        break
        