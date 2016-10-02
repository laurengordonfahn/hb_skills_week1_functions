# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def cost_w_tax(state_abv, cost, tax = 5):
    """ Function takes in three arguments: a string state abreviation, an integer item cost, an integer tax, with default of 5%. Return value is total cost as a float.
    Function has a code line to substitue tax to 7% if state_abv "CA" is put in. """
    state_abv = state_abv.lower()
    if state_abv == "ca":
        tax = .07
    total_cost = round(((cost * (tax * .01)) + cost), 2)
  
    
    return total_cost 

# Driver code for is_berry = pass
# cost_w_tax("CA", 5.00, 6)


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):
    """ Function takes in arguement fruit string returns a boolean.
    If strawberry, cherry, or blackberry returns True else False."""

    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False

# #Driver code for is_berry = pass
# print is_berry("strawberry")
# print is_berry("quince")

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit):
    """Function takes in arguement string fruit and runs function is_berry and if True returns 0 else returns 5.
    If fruit string is strwberry, cherry, or blackberry the shipping cost return will be 0 else 5. """ 
    if is_berry(fruit) == True:
        return 0
    else:
        return 5

#Driver code for shipping_cost = pass
# print shipping_cost("strawberry")
# print shipping_cost("quince")

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town):
    """ Function take in a string arguement home town and returns True if it is Delmar, NY else returns False."""
    if town == "Delmar, NY":
        return True
    else:
        return False
#Driver Code for is_hometown = pass
# print is_hometown("Delmar, MI")
# print is_hometown("Delmar, NY")

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first_name, last_name):
    """ Function takes in two strings first and last name and concatenates them returns 1 full name string."""
    return first_name + " " + last_name

#Driver code for full_name = pass
# print full_name("Lauren", "Gordon-Fahn")
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(town, first_name, last_name):
    """ Function takes uses is_hometown, full_name function and three argument strings  home town name, first-name, last_name prints greeting string depending on if the home_town is shared. 
    Return value is None."""

    if is_hometown(town) == True:
        print "Hi, {}, we're from the same place!".format(full_name(first_name, last_name))
    else:
        print "Hi, {}, where are you from?".format(full_name(first_name, last_name))
#Driver code hometown_greeting = pass
# print hometown_greeting("Delmar, NY", "Lauren", "Gordon-Fahn")
# print hometown_greeting("Delmar, CA", "Lauren", "Gordon-Fahn")

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
#NOTE LOGIC local if we don't feed a y variable in to the add function some time before add(y) function the function will not run, so our option are to have it set inside the increment function, have a raw_input request set equal to the variable name y inside the increment function or feed y in as a parameter to the increment funciton. If we don't have a x in the return add(y,x)  call function line x will always be 1 because of how the function add is defined with the x defaulted
def add(y, x = 1):
    return x + y

def increment(y, x = 1):
    """ Function takes in arguement integer x with defalut value 1. Containes function add with arguement integer y with defalut value 1. Return value is sum of x and y."""
   
    return add(y, x)

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.
addfive = increment(5, 5)

print increment(addfive, 20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def list_append(num_list, num):
    """Funciton takes in a list of numbers and an integer which gets appended to the number list and returns the appended list. """
    num_list.append(num)
    return num_list

#Driver code for list_append = pass
# print list_append([1, 2, 3], 4)


#####################################################################