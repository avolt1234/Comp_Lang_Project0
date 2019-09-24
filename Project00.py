
def test(letters):

    with open("words.txt", 'r') as wordFile:
        new_words = wordFile.readlines()

    # Returns the number of occurrences of each letter in letters
    checkerDict = combLetters(letters)

    # Contains the return list for the printout
    returnList = []

    for word in new_words:
        word = word.replace('\n', '')
        if len(word) == 7:
            if checker(word, checkerDict):
                returnList.append(word)
    print(returnList)


def checker(word, checkerDict):

    for letter in word:
        try:
            if word.lower().count(letter) > checkerDict[letter]:
                return False
        except KeyError:
            return False
    return True


def combLetters(letters):

    retDict = {}
    for item in letters:
        for letter in item:
            try:
                retDict[letter] += 1
            except KeyError:
                retDict[letter] = 1
    return retDict

test(("pbcdefg",  "aedofg", "agog", "plenty"))
