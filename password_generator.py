import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


def generatepassword(nr_letters, nr_symbols, nr_numbers):
	total = nr_letters + nr_numbers + nr_symbols

	passwordlist = []

	for _ in range(1, nr_letters + 1):
		lol = random.choice(letters)
		passwordlist.append(lol)

	for _ in range(1, nr_symbols + 1):
		lmao = random.choice(symbols)
		passwordlist.append(lmao)

	for _ in range(1, nr_numbers + 1):
		rofl = random.choice(numbers)
		passwordlist.append(rofl)

	finalpassword = ""

	random.shuffle(passwordlist)

	for i in passwordlist:
		finalpassword += i

	return(finalpassword)


# print(generatepassword(4,4,4))