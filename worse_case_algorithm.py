from Validation_answer import validation_answer


def generate_feedbacktable(all_guesses):
    """creates a 2d table out of all possible guesses and the potential feedback and adds how often it occurs

     all_guesses = all possible guesses that can be made

     returns a table with the amount of how often the feedback occurs for the feedback"""
    combinations = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),
                    (3, 0), (4, 0)]  # all possible feedback
    table = []
    for i in all_guesses:
        row = [0] * len(combinations)
        for j in all_guesses:
            feedback = validation_answer(i, j)
            row[combinations.index(feedback)] += 1
        table.append(row)
    return table


def worstcase(table, all_guesses):
    """takes the table from generate_feedbacktable and places the highest values in a list and picks the lowest
    number out of the list

    table = the generated table with how often feedback occurs for a possible guess
    all_guesses = all possible guesses that can be made

    returns the lowest number from the list of the highest values
    """
    highist_values = []
    for i in table:
        highist_values.append(max(i))
    index_worsecase = highist_values.index(min(highist_values))
    return all_guesses[index_worsecase]
