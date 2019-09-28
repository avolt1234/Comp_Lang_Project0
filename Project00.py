import unittest


"""

"""

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

    # create a list of letters that are 7 in length, then use that list to call function checker which will return True if
    # the word passes the criteria or validation for the project. Join all these words using the .join function to print
    # out into the console
    print(', '.join([x.lower() for x in [x.replace('\n', '') for x in new_words if len(x.replace('\n', '')) == 7] if checker(x, checkerDict)]))
    return ', '.join([x.lower() for x in [x.replace('\n', '') for x in new_words if len(x.replace('\n', '')) == 7] if checker(x, checkerDict)])


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
            if word.lower().count(letter.lower()) > checkerDict[letter.lower()]:
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

# class to run test harness for Project 1
class Project1Testing(unittest.TestCase):

    def test1(self):
        self.assertEqual(test(("zymomin" "omixa")), "azimino, mammoni, maximin, maximon, minimax, monimia, monomya, zymomin", "Test1 Passed")

# Call the test function
#test(("zymomin" "omixa"))

# Call the testing function for test
unittest.main()


