# Major-Assignment
Python Semester 1 major assignment

Question 1 (20%): A simple sales records management system (Back to Beginning)
Western Wholesales Pty Ltd sells variety of products to the re-seller markets. It sells products in the following 6 categories: food, alcohol and beverage, apparel, furniture, household appliances, and computer equipment. Design a program to manage the sale records of the company and implement the program in Python programming language.

These sales records are stored in two CSV files, on for the customer details and the other for the records of sales to these customers.

The first file contains the customer records. Each customer record consists of following information: the customer id cust_id, the customer's name, the customer's postcode, the customer's phone number. In each record, only the customer's ID and name are required. Other details are optional (empty). Note, the customer id is a 6-digit number starting from 100000.

The second file contains the sale records. Each record contains the details of one sale, including date, trans_id, cust_id, catetegory, and value. Note the transaction id (trans_id) is a 9-digit number starting from 100000000.

Design a program and implement it in Python programming language that would load the customer records and sales records from two CSV files and then store the customer and sales details in a single data structure in the computer memory.

The two file names/paths can be optionally supplied as two command line arguments, with customer records file comes first, followed by the sales records file.

The program repeatedly displays a menu to allow the user to perform the following operations:

1. Load customer and sales records from two CSV files and store them in a single data structure. If there is already a data structure containing customer and sales records in the memory (either via the two CSV files from the command line or from a previous load customer and sales records menu option), the new customer and sales records from two new files would replace the existing customer records and the sales records in the computer memory. The program should prompt the user to provide the names/paths of the two new CSV files.

2. Save all customer records from the memory to a CSV file. Your program should prompt the user to provide a file path. If the file does not exist, create a new file. If the file does exist, warn the user that the content of the file would be lost and give the user the option of either changing the file name or cancel the operation. If the user decides to overwrite the file, save the customer records to that CSV file. The saved customer records file should have the same structure as that of the sample customer records file customers.csv. If there are no customer and sales records in the memory, inform the user and return to the main menu.

3. Save all sales records from the memory to a CSV file. Your program should prompt the user to enter a file path. If the file does not exist, create a new file. If the file does exist, warn the user that the content of the file would be lost and give the user the option of either changing the file name or cancel the operation. If the user decides to overwrite the file, save the sales records to that CSV file. The saved sales records file should have the same structure as that of the sample sales records file salles.csv. If there are no customer and sales records in the memory, inform the user and return to the main menu.

4. Quit the program.

Restrictions:

in this question, do not use ndarrays to store the customer records or sales records.
Recommendations:

You may use Python's builtin module csv to handle CSV files.
For your convenience, I have created two test files customers.csv and sales.csv. The customer records file contains the details of 200 customers while the sales records file contains 1000 sales records. The information inside the files are completely fititious and were randomly generated.

You are required to provide test evidence in your assignment documentation that your program was tested successfully using the above test files

You should test your program using multiple test data sets. You may create a few small test data sets of your own, perhaps containing a dozen customers and several dozens of sales records, and use these small test data sets to test your program first. Once your program works correctly with these small test data sets, you should then test your program using the above large test data set.

When creating your own test files, use the same column names as in customers.csv and sales.csv.
