def allguesses_generator():
    """makes a list with all possible guesses

     returns the list with all possible guesses"""
    celing = 6
    allGuesses = []
    for a in range(celing):
        for b in range(celing):
            for c in range(celing):
                for d in range(celing):
                    allGuesses.append([a, b, c, d])
    return allGuesses
