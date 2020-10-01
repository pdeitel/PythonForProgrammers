# fig02_01.py
"""Compare integers using if statements and comparison operators."""

print('Enter two integers and I will tell you', 
      'the relationships they satisfy.')

# read first integer
first_integer = int(input('Enter first integer: '))

# read second integer
second_integer = int(input('Enter second integer: '))

if first_integer == second_integer:
    print(first_integer, 'is equal to', second_integer)

if first_integer != second_integer:
    print(first_integer, 'is not equal to', second_integer)

if first_integer < second_integer:
    print(first_integer, 'is less than', second_integer)

if first_integer > second_integer:
    print(first_integer, 'is greater than', second_integer)

if first_integer <= second_integer:
    print(first_integer, 'is less than or equal to', second_integer)

if first_integer >= second_integer:
    print(first_integer, 'is greater than or equal to', second_integer)

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
