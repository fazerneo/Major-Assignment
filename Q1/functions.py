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

def other_options(user_input):
    if user_input == 1:
        return option1()
    elif user_input == 2:
        return option2()
    elif user_input == 3:
        return option3()
    
def option1():
    file1_name = input("please provide the filename or filepath of customer records:")
    file2_name = input("please provide the filename or filepath of Sales record:")
    with open(file1_name, "x") as file1, open(file2_name, "x") as file2:
        reader1 = file1.read()
        reader2 = file2.read()
        lines = reader1.readlines()
        return print(lines)
    
def option2():
    print("no")
    
def option3():
    print("ok")
    
        
        

