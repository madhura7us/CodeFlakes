# This program checks if a string is a palidrome
# A palindrome is a word that reads the same forwards and backwards
# For example, 'MOM', 'DAD', 'CIVIC'

myString = input("Enter a string")
print("You entered: ", myString)

revString = myString[:: -1] #one of the easiest ways to reverse a string in Python
print("The reverse is: ", revString)

if(myString == revString):
	print(myString, "is a palindrome")
else:
	print(myString, "is not a palindrome")