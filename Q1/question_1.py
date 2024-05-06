from functions import menu, other_options

Loaded_records = {}

while True: 
    user_input = menu()
    user_input = int(user_input)
    if user_input == 4:
        print("\nThank you for using the program")
        break
    else:
        other_options(user_input)
    
    