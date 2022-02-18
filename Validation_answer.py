import copy


def validation_answer(secretcode, guess):
    """ ensuring that every guess you make you get the correct feedback for it

    secretcode = the generated code which needs to be cracked 4 long between 0/5
    guess = made guess by the player/algorithm 4 long between 0/5

    returns feedback on the form (x,y) where x = right number and right position y = right number but wrong place
    """
    code = copy.copy(secretcode)
    LOCodeList = []
    LOGuessList = []
    BP = 0
    WP = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            BP += 1
        else:
            LOGuessList.append(guess[i])
            LOCodeList.append(code[i])

    for LOCodeListItem in LOCodeList:
        if LOCodeListItem in LOGuessList:
            LOGuessList.remove(LOCodeListItem)
            WP += 1

    return BP, WP
