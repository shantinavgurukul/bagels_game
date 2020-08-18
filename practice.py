import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    print (secretNum)
    return secretNum
def getClues(guess, secretNum):
    if str(guess) == secretNum:
        return 'You got it!'
        # break
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
        else:
            clue.append("none")
            # return 'None'
    return ' '.join(clue)
def isOnlyDigits(numsecretNum):
    if secretNum == 'none':
        return False

    for i in secretNum:
        if int(i) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
def playAgain():
    play = input("Do you want to play again? Yes or No?") 
    # return play.lower.startswith('y')
    return play=="yes"
NUMDIGITS = 3
MAXGUESS = 10
# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
# print('Here are some clues:')
# print('When I say:    That means:')
# print('  Pico         One digit is correct but in the wrong position.')
# print('  Fermi        One digit is correct and in the right position.')
# print('  None       No digit is correct.')

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have thought up a number. You have %s guesses to get it.', (MAXGUESS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
        while len(secretNum) == NUMDIGITS or isOnlyDigits(secretNum):
            guess = input("Guess Again=")

            # print(type(guess))
            # print ('Guess', + (numGuesses))
            clue = getClues(guess, secretNum)
            print(clue)


        #     # guess = int(input("Guess Again="))
        #     # clue = getClues(guess, secretNum)
        #     print(clue)
        #     numGuesses += 1
            if guess == int(secretNum):
                print("we are winner")
                # break
            elif numGuesses > MAXGUESS:
                print ('You ran out of guesses. The answer was ' + secretNum)
                # break
            else:
                numGuesses = numGuesses + 1
        if guess == int(secretNum):
            break
    if not playAgain():
        break
                
playAgain=input("do you want play again=")
if playAgain=='y':
    print("shanti")
        # break
elif playAgain=='n':
    print("not")
    # break

            
    