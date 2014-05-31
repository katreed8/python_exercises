# Expressions
#
# These are basically statements that evaluate to something.  So,
# 1 + 1 will turn into 2.
#

1 + 1  # becomes 2

2 * 7  # becomes 14

8 / 2  # becomes 4

5 - 2  # becomes 3

# Printing stuff out
#
# print() will print out whatever is in the brackets

print(1 + 1)  # prints out 2

# Data Types
#
# You can have different types of data.
# 1 is a number.  "hslkdfjsd" is a string (letters strung together). [1, 2, 3] is a list!
# Use type(thing) to find out what type thing is.

print(type( 1 )) # will tell you that is an integer (a kind of number)

print(type( "klsdjfs" )) # will tell you that is is a str (short for string)


# Variables
#
# You can put data in a box, and then call that box something.  Later on,
# you can see what is inside that box, or put something else into it.

x = 1 # creates a box called x, and puts the number one in it

my_list = [] # creates a box called my_list, and puts an empty list in it

x = "gksdjfklsd" # replaces what was in the box x, with the string "gksdjfklsd"

y = 0
y = y + 1 # adds 1 to whatever y was (evaluates what is on the right first, and then puts that into the box y)

# Testing for the truth!
#
# ==  --> are they the same?
# !=  --> are they different?
# >   --> is something bigger than something else?
# <   --> is something smaller than something else?
# >=  --> is something bigger or the same as something else?
# <=  --> is something smaller or the same as something else?

1 == 1 # evaluates to true, because they are the same!

1 != 1 # evaluates to false, because they are the same

9 > 4  # evaluates to true, because 9 is greater than 4

# Making Decisions
#
# You can do different things based on what you tested.
# Use if to do this.

if 1 == 1: # the colon is important
    print("1 is equal to 1") # notice the indent, not putting this in is an error!
else:
    print("1 is not equal to 1?!?!?!")

elif 2 == 2: # else if; use inbetween if and else to check for more things
    print("2 is equal to 2")

# Looping Around
#
# To do something more than once, you need a loop.

x = 0 # creates a box called x, and puts the number zero in it

while x < 4: # if x is less than 4, run the code below me
    print("x is less than 4") # well, yes it is!
    x = x + 1 # add one to whatever x is, then go back to the while loop

# Looping over lists
#
# You can do something for each element in the list

l = [1, 2, 3, 4, 3, 2, 1]

for item in l: # so for each item in the list l, run the code below
    print( item ) # item is a box that contains whatever thing in the list you are currently looking at



