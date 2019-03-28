import random
guessMe = random.randrange(1, 100)

count = 0
isCorrect = False

while count < 8 and not isCorrect:
    guess = int(input("Guess: "))
    if guess < guessMe:
        print("Higher")
        count = count + 1
    elif guess > guessMe:
        print("Lower")
        count = count + 1
    else:
        print("Correct!")
        isCorrect = True

if count == 8:
    print("Answer was: " + guessMe)