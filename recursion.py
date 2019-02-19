# Joining strings in an array
def join_array(array_of_strings):
	if len(array_of_strings) == 1:
		return array_of_strings[0]
	return join_array(array_of_strings[:-1]) + " " + array_of_strings[-1]

joined_array = join_array(["shine", "on", "you", "crazy", "diamond"])
print(joined_array)

# Finding the factorial
def num(n):
	if n == 1:
		return 1
	return num(n - 1) * n

factorial = num(12)
print("The factorial is {}".format(factorial))


