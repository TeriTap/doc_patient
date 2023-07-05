"""
Program: doctor.py
Author: Teri  07.05.23

Conducts an interactive session of nondirective psychotherapy.
"""

import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.", "Go on, go on.", "Hmmm...", "I understand", "If you say so.")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ", "That makes you feel ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "you":"I"}

# definition of the reply() function
def reply(sentence):
	"""Builds and returns a reply to the user input."""
	probability = random.randint(1, 4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)

# definition of the changePerson() function
def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns."""
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))

	return " ".join(replyWords)

# definition of the main() function
def main():
	"""Handles the interaction between patient and doctor"""
	print("Good morning. I hope you are well today.")
	print("What can I do for you?")
	while True:
		sentence = input("\nType your response or QUIT to exit >>")
		if sentence.upper() == "QUIT":
			print("Have a nice day!")
			break
		print(reply(sentence))

# Global call to main() for program execution
if __name__ == '__main__':
	main()