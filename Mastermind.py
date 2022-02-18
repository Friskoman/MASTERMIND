import random
from Possible_sollutions import generate_feedbacktable, worstcase
from all_combinations import allguesses_generator
from Mastersolver_simpleAI import consistent_guesses
from Validation_answer import validation_answer
from Spice_algoritme import start_guesses


def secret_code_generator():
    """creates a list of 4 long with a random int between 0/5 for every index

    returns the set list of 4 random numbers between 0/5"""
    secret_code = []
    while len(secret_code) != 4:
        x = random.randint(0, 5)
        secret_code.append(x)
    return secret_code


def guess_input_player():
    """asks a input of 4 long with a value of 0/5 for every index

    returns the the input"""
    while True:
        guess = (input('try to crack te secret code \n'
                       ' your guess can only be between 0/5 and needs to be 4 long\n'))
        if len(guess) != 4:  # makes sure that the input is exactly 4 long
            print('Sorry, pleas make a valid guess')
            continue
        else:
            break

    valid_guess = [int(i) for i in guess]  # chops the input in to a list

    return valid_guess


def game_loop():
    """ this is the main loop where the game is functioning in"""
    all_guesses = allguesses_generator()
    secretcode = secret_code_generator()
    counter = 1
    while True:
        menu = int(input(     # menu for which algorithm you wanna play or play it yourself
            'wich of the 3 stragaties would you like to run?\n'                                 
            '0. Brain\n'  
            '1. Simple\n'
            '2. worst case\n'
            '3. spice\n'))
        if menu > 3 or menu < 0:
            continue
        else:
            break
    while counter != 11:
        print('try', counter)
        if menu == 0:  # player vs computer
            guess = guess_input_player()

        elif menu == 1:  # simple algorithm vs computer
            guess = all_guesses[0]

        elif menu == 2:  # worse case algorithm vs computer
            feedbacktable = generate_feedbacktable(all_guesses)
            guess = worstcase(feedbacktable, all_guesses)

        else:  # own made algorithm vs computer
            if counter < 4:
                guess = start_guesses(counter)
            else:
                guess = all_guesses[random.randint(0, len(all_guesses) - 1)]
        game_feedback = validation_answer(secretcode, guess)
        if menu != 0:
            all_guesses = consistent_guesses(guess, all_guesses, game_feedback)
        print(game_feedback)
        counter += 1
        if game_feedback == (4, 0):  # checks if you've cracked the code and end the game afterwards
            print('you have cracked the code')
            exit()
    print('you have failed to crack the code\n'
          'the code is', secretcode)
    exit()


game_loop()
