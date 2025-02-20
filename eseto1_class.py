"""
Date: 6/19/2024

This is the user-defined class that is to be imported into final project file
that manipulates the user's shopping list.
"""

# One user-defined class
class Shopping:
    '''User shopping list'''
    
    def __init__(self, shopping_dict): # An init() class method
        '''Initialize the shopping list'''
        
        self.__shopping_dict = shopping_dict 
        # Private self class attribute
        self.items = list(shopping_dict.keys()) 
        # Public self class attribute
        self.costs = list(shopping_dict.values()) 
        # Public self class attribute
        
    
    def __shop_dictionary(self): # Private class method
        '''Method for getting a string of the items and a dollar ($) before
        the cost'''
        item_cost_str = ', '.join("'{}': ${}".format(keys, values) 
                        for keys, values in self.__shopping_dict.items())
        return str(item_cost_str)
    
    def total_cost(self): # Public class method
        '''Method to get the total cost of all items'''
        for i in range(0, len(self.costs)):
            self.costs[i] = float(self.costs[i])
        self.total = sum(self.costs)
        return self.total
    
    def get_item(self, user_input2): # Public class method
        '''Method to get cost of an item the user wants to take out of the
        shopping list (user_input2)'''
        try:
            cost = self.__shopping_dict[user_input2]
        except KeyError:
            cost = None
        return cost
    
    def __remove_item(self, user_input2): # Private class method
        '''Method to remove the user input from the dictionary'''
        self.__shopping_dict.pop(user_input2)
        return self.__shopping_dict.keys()

    def __sub__(self, user_input2): # Magic class method
        '''Method to get the recalculated cost after an item is taken off the 
        shopping list'''
        new_total =float(self.total) - float(self.__shopping_dict[user_input2])
        return new_total
    
       
    def __repr__(self): # A repr() class method 
        '''Method to return the items as a string after first converting it
        to a set'''
        return str(set(self.__shopping_dict.keys())) # Set




