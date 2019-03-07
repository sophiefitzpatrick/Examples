# simple examples of break, continue and pass


number = 0

for number in range(15):
	number = number + 1

	if number >= 10:
		break # stops the loop once the number becomes greater than or equal to 10
	print(number)

print("out of loop")


for number in range(15):
	number = number + 1

	if number == 12:
		continue # if the number is equal to 12, the loop continues
	print(number)

print("out of loop")

for number in range(15):
	number = number + 1

	if number < 12:
		pass # passes the if statement, and runs the loop anyway
	print(number)

print("out of loop")