import unittest


"""
Student: Alexander Voultos
Class: CS-3180-01

CONTRACT: find-words : letters -> String
   PURPOSE: Returns a string of comma delimited dictionary words 7
   letters long and in alphabetical order that can be composed of
   characters in letters. (anagrams of letters) There is no trailing
   comma after the last word in the returned string.
   Each letter in letters may only be used once per match, e.g.
   (find-words '("zymomin" "am")) could return "mammoni, zymomin"
   because "mammoni" is composed of letters in letters including the
   three 'm' characters in letters, and "zymomin" is similarly composed of
   letters in letters. However, "mammomi" could not be
   returned because "mammomi" requires four 'm' characters and
   only three are available in letters
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
            # Checks for the total number of characters in the letter vs parameters
            if word.lower().count(letter.lower()) > checkerDict[letter.lower()]:
                # If the word count is greater than parameter, return False which means the word did not pass validation
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
        # Parse through the characters in the String
        for letter in item:
            # If the character is a key in the dictionary, append the item in the dict by 1
            try:
                retDict[letter] += 1
            # If the character is not a key in the dictionary, create one and set the item to 1
            except KeyError:
                retDict[letter] = 1
    return retDict

# Call the test function
test(("zymomin" "omixa"))



