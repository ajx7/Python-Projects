import random

#get guess
def get_guess():
	return list(input("What is your guess? "))


#generate computer code
def generate_code():
	digits=[str(num) for num in range(10)]

	#suffle the digits
	#then grab the first three
	return digits[:3]


#generate clues

def generate_clues(code, guess):

	if(guess == code):
		return "CODE CRACKED!"

	clues = []

	for i,num in enumerate(guess):
		if num == code[i]:
			clues.append("match")

		elif num in code:
			clues.append("close")

	if clues==[]:
		return["Nope"]

	else:
		return clues


#game logic

print("Welcome cCode Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":
	guess = get_guess()

	clue_report = generate_clues(secret_code,guess)

	print("Here is result of your guess: ")
	for clue in clue_report:
		print(clue)