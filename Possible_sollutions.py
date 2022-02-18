from Validation_answer import validation_answer


def generate_feedbacktable(all_guesses):
    combinations = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),
                    (3, 0), (4, 0)]
    table = []
    for i in all_guesses:
        row = [0] * len(combinations)
        for j in all_guesses:
            feedback = validation_answer(i, j)
            row[combinations.index(feedback)] += 1
        table.append(row)
    return table


def worstcase(table, all_guesses):
    highist_values = []
    for i in table:
        highist_values.append(max(i))
    index_worsecase = highist_values.index(min(highist_values))
    return all_guesses[index_worsecase]
