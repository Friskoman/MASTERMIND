from Validation_answer import validation_answer


def consistent_guesses(guess, all_guesses, game_feedback):
    """filters all Inconsistent guesses out of the list of all guesses and append them to a new list

    guess = the last made guess by the player/algorithm
     all_guesses = all possible guesses that can be made
    game_feedback = the given feedback for the last guess

    returns a list with possible consistent guesses """
    possible_all_guesses = []
    for i in all_guesses:
        feedback = validation_answer(guess, i)
        if feedback == game_feedback:
            possible_all_guesses.append(i)
    print(possible_all_guesses)
    return possible_all_guesses
