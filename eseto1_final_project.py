"""
Date: 6/19/2024
Expense Tracker

Description of Problem:
The user will input the specific shopping list file to read with the format 
being (1) Item, (2) Quantity, (3) Cost each($) on each line, separated by
commas. The user will then enter their maximum dollar ($) amount limit they
wish to spend and given the total cost calculated from the file, the user may
be asked to remove an item. The new total amount to be spent will be calculated 
and if it is below the limit, a congratulations message will output; if it is
above the limit an error message will print.
"""

from eseto1_class import Shopping
import os
import sys


# One user-defined function
def shopping_list_converter(file_list):
    '''Converts the lists created from the user shopping list file into a
    dictionary; with the dictionary {item, total cost}'''
    
    # Create separate lists from each header on the first line of the .txt file
    # (1) Item, (2) Quantity, (3) Cost each($)
    items_list = file_list[3::3]
    items_list2 = [item.lower() for item in items_list] #lowercase
    quantity_list = file_list[4::3]
    cost_each_list = file_list[5::3]
   
    # Determine the total cost of each item given the quantity wanted
    # One try block with else condition
    try:
        total_cost_list = []
        for i in range(0, len(quantity_list)):
            user_calc_float=float(quantity_list[i])*float(cost_each_list[i])
            total_cost_list.append("%.2f" % user_calc_float)
            # Gets cost written as a number with two decimal places
            
    except ValueError:
        print("--> ValueError: Not all values for quantity and cost"
              + " are numbers.")
        sys.exit()
        # Prints error if quantity and costs from txt file are not numbers
        
    else:
        shop_tuple = [(key, value) for i, (key, value) 
                      in enumerate(zip(items_list2, total_cost_list))] # Tuple

        # Dictionary    
        shop_dictionary = dict(shop_tuple)
        return shop_dictionary
    
      
if __name__ == '__main__':         
    # while loop
    while True:
        # Ask the user for their spending limit
        user_input = input("Please enter the max limit, as a whole number ($)," 
                       + " you want to spend during this shopping trip: ")

        user_input = user_input.replace("$", "", 1) 
        # Removes $ symbol once if used
    
        # if statement
        if user_input.isdigit() != True:
            print("Input is not a valid whole number. Please try again.")
            continue
            # Example Output:   
            # Please enter the max limit, as a whole number ($), you want to 
            # spend during this shopping trip: $$234
            # Input is not a valid number. Please try again.
            
        else:
            # One input file (included input data with project)
            # User is to state the name of the text file with the shopping list
            # in the correct format, if incorrect file, user will have to start
            # from the beginning
            input_file_str = input("Enter a file name of text words: ")
            file_exist = os.path.exists(input_file_str)
            if file_exist is False:
                print("File does not exist. Please try again.")
                continue
                # Example Output:
                # Enter a file name of text words: hello
                # File does not exist. Please try again.
            
            else:
                # Read the file
                input_file_to_read = open(input_file_str, "r")
                file_content_str = input_file_to_read.read() 
            
            
                # Remove all "\n"=new lines (leaving a comma between words)
                file_content_str = ', '.join(file_content_str.splitlines())
                
                # Convert the words to a list
                file_list = list(file_content_str.split(", ")) # list
                # print(file_list) #check if words print to list correctly
                
                # Close the file that you are reading
                input_file_to_read.close()
                
                
                # Use user-defined function with data from txt file
                shopping_dict = shopping_list_converter(file_list)
                
                # Use the class imported from other .py file and value from
                # the user-defined function
                cart = Shopping(shopping_dict)
                
                # Provide 2 unit tests that prove class methods work as 
                # expected.
                cart._Shopping__remove_item('tissues')
                assert cart.get_item('tissues') == None
                        
                cart._Shopping__remove_item('soap')
                assert cart.get_item('soap') == None
                     
                # Check if both unit tests are successful
                print("--> Unit test successful")
                
                
                # Code to print outputs are below
                shopping_dict = shopping_list_converter(file_list)
                
                cart = Shopping(shopping_dict)
                
                print("Total cost of each item, given quantity needed to buy: " 
                  + str(cart._Shopping__shop_dictionary()))
            
                print("Total cost of shopping trip is: $" 
                      + str(cart.total_cost()))
                
                if int(user_input) < cart.total_cost():
                    print("Total cost of items is greater than your maximum" 
                          + " spend limit.")
                    
                    user_input2 = input("Please enter an item to take out: ")
                    user_input2 = user_input2.lower()
                    
                    if user_input2 not in shopping_dict:
                        print("Error, item not in list. Please try again.")
                        sys.exit()
                        # Program quits if user input is not valid
                        # Example Output:
                        # Please enter an item to take out: towels
                        # Error, item not in list. Please try again.
                        
                    else:
                        if int(user_input) < cart.__sub__(user_input2):
                            print("Total cost of items: $" 
                              + str(cart.__sub__(user_input2) )
                              + " is still greater than" 
                              + " your maximum spend limit. Please revise your" 
                              + " list and try again.")
                            sys.exit()
                            # If after taking out an item from the shopping 
                            # cart and the total is still greater than the user 
                            # input, the program will print the output above 
                            # and quit
                            
                        else:
                            print("Congrats! Item total: $" 
                              + str(cart.__sub__(user_input2))
                              + " is less than your maximum spend limit!")
                            cart._Shopping__remove_item(user_input2)
                            print("Final shopping list: " + repr(cart))
                            sys.exit()
                            # Prints new total and final shopping list
                else:
                    print("Congrats! Item cost total is less than your maximum" 
                          + " spend limit!")
                    sys.exit()
        

# Example Output 1
# Please enter the max limit, as a whole number ($), you want to spend during 
# this shopping trip: 90
# Enter a file name of text words: eseto1_project.txt
# --> Unit test successful
# Total cost of each item, given quantity needed to buy: 'soap': $7.98, 
# 'tissues': $4.99, 'vitamins': $20.98, 'trash bags': $25.00, 
# 'eggs (a dozen)': $10.00, 'cereal': $23.94
# Total cost of shopping trip is: $92.89
# Total cost of items is greater than your maximum spend limit.
# Please enter an item to take out: ViTAMins
# Congrats! Item total: $71.91 is less than your maximum spend limit!
# Final shopping list: {'tissues', 'eggs (a dozen)', 'cereal', 'soap', 
# 'trash bags'}


# Example Output 2
# Please enter the max limit, as a whole number ($), you want to spend during 
# this shopping trip: $100
# Enter a file name of text words: eseto1_project.txt
# --> Unit test successful
# Total cost of each item, given quantity needed to buy: 'soap': $7.98, 
# 'tissues': $4.99, 'vitamins': $20.98, 'trash bags': $25.00, 
# 'eggs (a dozen)': $10.00, 'cereal': $23.94
# Total cost of shopping trip is: $92.89
# Congrats! Item cost total is less than your maximum spend limit!


# Example Output 3
# Please enter the max limit, as a whole number ($), you want to spend during 
# this shopping trip: 50
# Enter a file name of text words: eseto1_project.txt
# --> Unit test successful
# Total cost of each item, given quantity needed to buy: 'soap': $7.98, 
# 'tissues': $4.99, 'vitamins': $20.98, 'trash bags': $25.00, 
# 'eggs (a dozen)': $10.00, 'cereal': $23.94
# Total cost of shopping trip is: $92.89
# Total cost of items is greater than your maximum spend limit.
# Please enter an item to take out: soAp
# Total cost of items: $84.91 is still greater than your maximum spend limit. 
# Please revise your list and try again.












