# This program counts the number of vowels in a string

from collections import Counter
myString = input("Enter a string: ")

allCount = Counter(myString)
print("Total letter count is: ", allCount)

vowels = allCount['a'] + allCount['e'] + allCount['i'] + allCount['o'] + allCount['u']

print("The number of vowels is: ", vowels)
