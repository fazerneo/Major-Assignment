from functions import menu, option1, print_dict

Loaded_records = {}

while True: 
    user_input = menu()
    user_input = int(user_input)
    
    if user_input == 1:
        Loaded_records = option1(Loaded_records)
        
        print_dict(Loaded_records)
    
    elif user_input == 4:
        print("\nThank you for using the program")
        break
        