# FizzBuzz is a game where numbers from 1 to 100 are taken and 
# 1. if the number is divisible by 3, write "fizz"
# 2. if the number is divisible by 5, write "buzz"
# 3. if the number is divisible by both 3 and 5, write "fizzbuzz"
# 4. Otherwise, write the number as it is

for i in range(1, 100):
	if(i%15 == 0):
		print("fizzbuzz")
	elif(i%5 == 0):
		print("buzz")
	elif(i%3 == 0):
		print("fizz")
	else:
		print(i)
