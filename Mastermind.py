import copy
import random

def secret_code_generator():
    secret_code = []
    while len(secret_code) != 4:
        x = random.randint(0, 5)
        secret_code.append(x)
    return secret_code

def guess_input_player():
    valid_guess = []
    while True:
        guess = (input('try to crack te secret code \n'
                          ' your guess can only be between 0/5 and needs to be 4 long\n'))
        if len(guess) != 4:
            print('Sorry, pleas make a valid guess')
            continue
        else:
            break

    for i in guess:
        valid_guess.append(int(i))
    return (valid_guess)

def validation_answer(secretcode, guess):
    code = copy.copy(secretcode)
    LOCodeList = []
    LOGuessList = []
    BP = 0
    WP = 0
    for i in range(len(code)):
        print(code[i], guess[i])
        if code[i] == guess[i]:
            BP +=1
        else:
            LOGuessList.append(guess[i])
            LOCodeList.append(code[i])
    for LOCodeListItem in LOCodeList:
        if LOCodeListItem in LOGuessList:
            LOGuessList.remove(LOCodeListItem)
            WP += 1

    if BP == 4:
        print('you have cracked the code')
        exit()
    return (BP, WP)


def try_counter():
    secretcode = secret_code_generator()
    print(secretcode)
    counter = 0
    while counter != 10:
        print('try', counter+1)
        guess = guess_input_player()
        print(validation_answer(secretcode, guess))
        counter += 1
    print('you have failed to crack the code')

try_counter()
