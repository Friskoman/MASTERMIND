import copy


def validation_answer(secretcode, guess):
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
