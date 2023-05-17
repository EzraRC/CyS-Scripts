#get input from user
userInput = input('Enter your input: ')

print('Your input in reverse is: ')

#print in reverse
for i in range(0, len(userInput)):
	print(userInput[len(userInput) - i - 1], end = "")
