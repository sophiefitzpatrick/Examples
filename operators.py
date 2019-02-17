# Indexing, Concatenation, Slicing
def lcohen():
	lcohen = "the last time we saw you, you looked so much older, your famous blue raincoat was torn at the shoulder"
	index_ten = lcohen[10] # indexing
	print(index_ten)
	index_raincoat = lcohen[69:78] # slicing
	index_torn = lcohen[82:87]
	print(index_torn + index_raincoat) # concatenation

lcohen()

# Index Deletion, Index Assignment
def dogs():
	best_boys = ["rua", "murphy", "henry", "pop"]
	print(best_boys)
	del best_boys[2] # indexed deletion 
	print(best_boys)
	new_best_boy = "pig"
	best_boys[2] = new_best_boy # indexed reassignment
	print(best_boys)

dogs()

# Addition, Subtraction, Multiplication, Division, Modulo
def calculate(value):
	value = value
	addition = value + 25 # addition
	subtraction = addition - 27 # subtraction
	multiplication = subtraction * 99 # multiplication
	division = round(multiplication/31) # division
	print(division)
	modulo = division % 17 # modulo
	print(modulo)
	floor_division = multiplication // 15 # floor division
	print(floor_division)

calculate(54)

# Ordering, Equality, Difference
def equality(num1, num2):
	num1 = num1
	num2 = num2
	if num1 > num2: # ordering
		print("{} is greater than {}".format(num1, num2))
	elif num2 != num1: # difference
		print("{} is not equal to {}".format(num1, num2))
	elif num1 == num2: # equality
		print("%s is equal to %s" % (num1, num2)) # String Formatting
	else:
		print("bye")

equality(10,10)

# Truth Test
obj = 8
if obj:
	print("true")
else:
	print("false")

