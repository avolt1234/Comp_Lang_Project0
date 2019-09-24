
def test(letters):
    """
    Main function for Project0 python file
    :param letters: (Tuple) - Valid strings to be used for character validation
    :return:
    """
    with open("words.txt", 'r') as wordFile:
        new_words = wordFile.readlines()

    # Returns the number of occurrences of each letter in letters
    checkerDict = combLetters(letters)

    # Contains the return list for the printout
    returnList = []

    # If the word in new_words is longer than 7 and the word contains all valid chars, append to returnList
    for word in new_words:
        word = word.replace('\n', '')
        # Checks if the length of the word is equal to 7
        if len(word) == 7:
            if checker(word, checkerDict):
                returnList.append(word)
    print(returnList)


def checker(word, checkerDict):
    """
    Checker function for Project0
    :param word: (String) - String to check for validity
    :param checkerDict: (Dict) - Dictionary that contains the valid characters and max usage of those chars
    :return:
        True if passes validation
        False if fails validation
    """
    for letter in word:
        try:
            if word.lower().count(letter) > checkerDict[letter]:
                return False
        except KeyError:
            return False
    return True


def combLetters(letters):
    """
    Function that returns a dictionary of how many characters were used in the letters variable
    :param letters: (Tuple) - Tuple of strings used as valid letters
    :return:
    """
    retDict = {}
    for item in letters:
        for letter in item:
            try:
                retDict[letter] += 1
            except KeyError:
                retDict[letter] = 1
    return retDict

test(("pbcdefg",  "aedofg", "agog", "plenty"))
