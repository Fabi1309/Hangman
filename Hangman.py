import random

maxguesses = 15
actualguesses = 0

guessed = False

lettersguessed = list()
words = list(("spread","saw","method","difficulty","knew","roof","fastened","consonant","carried","realize"))
word = words[random.randrange(0,len(words))]
letters = list(word)
guesslength = len(letters)

print("The word contains ", guesslength, " characters. Good luck!")

guessvisual = "";

for x in range(guesslength):
	guessvisual += "_"

visuallist = list(guessvisual)

print("Your word: ", visuallist)

print()
print()

while(guessed == False):
	print()
	print()
	if(actualguesses < maxguesses):
		guessletter = input("Guess a letter: ")
		guessletterlist = list(guessletter)
		
		if(len(guessletterlist) != 1):
			print("Please input only one letter")
			guessed = False
		if(guessletter in lettersguessed):
				print("You have already used this letter!")
		if(len(guessletterlist) == 1):
			if(guessletter not in lettersguessed):


				if(guessletter not in letters):

					print("This letter is not in the word")
					actualguesses += 1
					print("You have ", maxguesses - actualguesses, " tries left")
					lettersguessed.append(guessletter)


				if(guessletter in letters):

					lettersguessed.append(guessletter)
					while(guessletter in letters):
						i = 0
						while (guessletter != letters[i]):
							i += 1
						i += 1
						print("This letter is in the word at position: ", i)
						letters[i-1] = "_"
						visuallist[i-1] = guessletter
					print("Your word: ", visuallist)

					if("_" not in visuallist):
						print("You have successfully guessed the word: ", word)
						guessed = True
						
	if(actualguesses == maxguesses):
		print("You have lost. The word was: ", word )
		guessed = True

