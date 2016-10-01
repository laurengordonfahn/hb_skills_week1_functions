"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """ Function takes no arguments prints "Hello World".
    Return value of None """
    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """ Function takes a string argument prints a string, Hi with name arguement appended. 
    Return value of None"""

    print "Hi {}".format(name)


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(num1, num2):
    """ Function takes two intergers as arguments prints the product of arguments.
    Return value is None."""
    print num1*num2

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(desired_string, multiplier):
    """ Function takes two arguements, a string and an integer, and prints the string as many times as integer value.
        Return value is None.
         """
    print desired_string*multiplier


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(num1):
    """ Function takes 1 integer argument and prints string message if higher or lower than 0.
    Return value is None"""
   
    if num1 > 0:
        print "Higher than 0"
    elif num1 < 0:
        print "Lower than 0"
    else:
        print "Zero"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(num1):
    """ Function takes 1 arguement integer with return value of a boolean (True or False) depending if arguement is divisible by 3."""
    if num1%3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(sentence):
    """ Function takes 1 string arguement with return value of an integer, representing the number of spaces in the sentence string argument."""
    num_spaces = 0
    for element in sentence:
        if element == " ":
            num_spaces +=1
    return num_spaces

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


def total_meal_price(meal_price, percent_tip = 15):
    """Function takes two float arguements a meal price and percent tip with return value being a float represenatation of the total meal price.
    if no percent tip is given 15 percent is the defalut"""
# BUG WAS DUE TO TEST ONLY WANTING TO TAKE ANSWER TO THE TENS PLACE
    
    tip = (.01 * percent_tip) * meal_price
    return round(meal_price + tip, .1)


   

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.

def sign_and_parity(number):
    """ Function takes 1 integer argument and returns a list containing two strings indicating if the arguement is positve or negative and even or odd."""
    
    num_character_list = []
    if number%2 == 0:
        num_character_list.append("Even")
    else:
        num_character_list.append("Odd")
    
    if number >= 0:
        num_character_list.append("Positive")
    else:
        num_character_list.append("Negative")

    return num_character_list
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def unpack_list(number):
    """Function takes an integer arguement and unpacks the sign_and_pariaty functions' returned list for this number.
    Function prints wheather arguement is postive or negative, even or odd. Return value None """
    sign, parity = sign_and_parity(number)

    print sign, parity

unpack_list(5)




################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.


def full_title(name, job_title = "Engineer"):
    """ Funciton takes a maxium of two string arguements a minumum of 1 a name and a job title, default Engineer, and returns the concatination. 
    """

    return job_title + " " + name

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(name, job_title, sender_name):
    print "Dear {}, I think you are amazing! Sincerely, {}".format(full_title(name, job_title), sender_name)

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
