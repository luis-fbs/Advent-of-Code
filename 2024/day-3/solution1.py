with open("filtered_input", "r") as file:
	numbers = [ int(number.split(",")[0]) * int(number.split(",")[1]) for number in file ]

print(sum(numbers))
