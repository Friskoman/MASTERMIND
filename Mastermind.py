import random
from Possible_sollutions import generate_feedbacktable, worstcase
from all_combinations import allguesses_generator
from Mastersolver_simpleAI import consistent_guesses
from Validation_answer import validation_answer
from Spice_algoritme import start_guesses


def secret_code_generator():
    secret_code = []
    while len(secret_code) != 4:
        x = random.randint(0, 5)
        secret_code.append(x)
    return secret_code


def guess_input_player():
    while True:
        guess = (input('try to crack te secret code \n'
                       ' your guess can only be between 0/5 and needs to be 4 long\n'))
        if len(guess) != 4:
            print('Sorry, pleas make a valid guess')
            continue
        else:
            break

    valid_guess = [int(i) for i in guess]

    return valid_guess


def try_counter():
    all_guesses = allguesses_generator()
    secretcode = secret_code_generator()
    counter = 1
    while True:
        choicemenu = int(input('wich of the 3 stragaties would you like to run?\n'
                               '1. Simple\n'
                               '2. worst case\n'
                               '3. spice\n'))
        if choicemenu > 4 or choicemenu < 0:
            continue
        else:
            break
    while counter != 11:
        print('try', counter)
        guess = []
        if choicemenu == 1:
            guess = all_guesses[0]

        elif choicemenu == 2:
            feedbacktable = generate_feedbacktable(all_guesses)
            guess = worstcase(feedbacktable, all_guesses)
        else:
            if counter < 4:
                guess = start_guesses(counter)
            else:
                guess = all_guesses[random.randint(0, len(all_guesses) - 1)]
        game_feedback = validation_answer(secretcode, guess)
        all_guesses = consistent_guesses(guess, all_guesses, game_feedback)
        print(game_feedback)
        counter += 1
        if game_feedback == (4, 0):
            print('you have cracked the code')
            exit()
    print('you have failed to crack the code\n'
          'the code is', secretcode)
    exit()


try_counter()
