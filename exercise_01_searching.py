# Can you look for my lost number?
#
# Fix the code so that it runs properly.

lost = 5

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.01
# print out "not this one" if the item isn't my lost number,
# or "found it!" if it is my lost number.

for item in l:
    if :
        print()
    else:
        print()

# 1.02
# stop going through the list once you found it

for item in l:
    if :
        print()
        break # stops going through the list
    else:
        print()

# 1.03
# Same thing, but a bit differently

x = 0

while x < len(l): # run the code while x is less than the length of the list
    if l[x]  :
        print()
        break
    else:
        print()

    x = x + 1

# 1.04
# What if you don't find it?  Infinite loops!
# Can you fix the code so that it doesn't run forever, but stops at the end of the list?

x = 0

while l[x] != lost:
    print("not this one")

    if : # hint: len(l) will be helpful
        break

# 1.05
# Can you make this a function?

def search_list(lost, wild_list): # takes a lost number and a wild list
    # step 1: go through the list, and do the checks (same as all the stuff above)
    # step 2: if you found it return the lost number (return lost)
    # step 3: if you never found it, return "sorry..."

print( search_list(1, [1, 2, 3]) ) # this should print out the number one

print( search_list(1, [7, 3, 5, 7]) ) # this should print out "sorry..."

print( search_list(0, []) ) # this should print out "sorry..."


