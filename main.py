import math
import random 
import datetime
from functions import *
# The * following this import means to import all the functions in the library. 
from myTime import *

# This is a comment... What purpose do comments serve in programming?
 
# PART 1: enterning your name 
name = input("What is your name: ")
print("Hi " + name)
getMinute()

# PART 2: entering your age
yourAge = input("How old are you: ")
# enter a number for the line above 
print("You are " + yourAge + " years old. Let's compare your age to Lucy's!")

# PART 3: exploring conditionals 
# declaring Lucy's age
lucyAge = 17;

#comparing your age with that of Lucy's. Lucy is 17 years old.  
# we need to add int() before our variable in order to convert the number into an integer--a whole number. We want both of our variables to be the same data-type value which means we want them both to be integers. 

if int(lucyAge) > int(yourAge): 
  print("Lucy is older than you!")
elif int(lucyAge) == int(yourAge):
  print("You and Lucy are the same age!")
elif int(lucyAge) < int(yourAge) : 
  print("You are older than Lucy!")

howOldIsLucy(lucyAge, yourAge)

#EXPLORE ACTIVITY



# After running the code and seeing how it works, remove the function call above for howOldIsLucy() and define and call that function yourself below this comment by follwoing the instructions found to the left in the file called ExploreFunctionInstructions.pdf

