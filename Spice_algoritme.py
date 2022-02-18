def start_guesses(counter):
    """ the first 3 guesses that the algorithm makes to know what numbers will be in the list

    counter = the amount of tries you have done already
    
    returns pre-made guess """
    if counter == 1:
        guess = [0, 0, 1, 1]
    elif counter == 2:
        guess = [2, 2, 3, 3]
    elif counter == 3:
        guess = [4, 4, 5, 5]
    return guess



