import csv
import os

def menu():
    ''' This function prints out a menu for the main program and gets user input,
    the user input is then returned for use in the main program '''
    
    print("Sales Records Management System\n")
    print("Please select an option below to get started")
    print("1. Load Customer and Sales Records")
    print("2. Save Customer Records")
    print("3. Save Sales Records")
    print("4. Quit Program")
    user_input = input("Type the number corresponding to your desired action: ")
    
    return user_input

        
        

