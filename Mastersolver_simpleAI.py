from Validation_answer import validation_answer


def consistent_guesses(guess, all_guesses, game_feedback):
    possible_all_guesses = []
    for i in all_guesses:
        feedback = validation_answer(guess, i)
        if feedback == game_feedback:
            possible_all_guesses.append(i)
    print(possible_all_guesses)
    return possible_all_guesses
