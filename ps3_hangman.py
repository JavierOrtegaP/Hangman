# Hangman game
import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
# Assigns the randomly chosen word to the variable secretWord so that all
# functions can access it
secretWord = chooseWord(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are
    in lettersGuessed;
      False otherwise
    example:
    >>> secretWord = 'apple'
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(isWordGuessed(secretWord, lettersGuessed))
    False
    '''
    # Returns False if the list of lettersGuessed is empty
    if lettersGuessed == []:
        return False
    # Else, check if any of the letters in secretWord is not in lettersGuessed.
    # If any is not included, return False. If all are included, return True
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    example:
    >>> secretWord = 'apple'
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getGuessedWord(secretWord, lettersGuessed))
    '_ pp_ e'
    '''
    # Assigns an empty string to guessed_
    guessed_word = ""
    # Checks each letter of secretWord; if the letter is included, add it to
    # guessed_word. If it's not, add a "_" instead
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what
    letters have not yet been guessed.
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getAvailableLetters(lettersGuessed))
    abcdfghjlmnoqtuvwxyz
    '''
    # Assigns an empty string to guessed_
    available_letters = ""
    # Imports a list of lowercase letters
    from string import ascii_lowercase
    # Checks each letter of the alphabet; if the letter is included in
    # lettersGuessed, add it to available_letters. If it's not,
    # don't add anything
    for letter in ascii_lowercase:
        if letter not in lettersGuessed:
            available_letters += letter
    return (available_letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!" + "\n" +
          "I am thinking of a word that is " +
          str(len(secretWord)) + " letters long." + "\n" + "-------------")

    # Create an empty list that will store the letters that the user has
    # already input as a guess
    lettersGuessed = []
    # Variable that shows how many guesses remain for the user; starts at 8
    guesses_left = 8
    # Store the last user guess
    user_guess = ""

    from string import ascii_lowercase

    while True:
        # If the user run out of guesses, print game over screen and restart
        # the game with a new word and and empty lettersGuessed list
        if guesses_left == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            print("Thanks for playing!" + "\n" + "-------------")
            secretWord = chooseWord(wordlist)
            guesses_left = 8
            print("Welcome to the game Hangman!" + "\n" +
                  "I am thinking of a word that is " +
                  str(len(secretWord)) + " letters long." +
                  "\n" + "-------------")
            lettersGuessed.clear()
            continue
        # If the user guessed the word correctly, end the game
        if isWordGuessed(secretWord, lettersGuessed) is True:
            print("Congratulations, you won!")
            return
        print("You have " + str(guesses_left) +
              " guesses left." + "\n" +
              "Available letters: " +
              getAvailableLetters(lettersGuessed))
        user_guess = input("Please guess a letter: ")
        user_guess_lowercase = str(user_guess.lower())
        # Error handling: triggers a message if the user doesn't input a
        # lowercase or uppercase letter included in ascii_lowercase
        while (len(user_guess_lowercase) != 1) or \
                (user_guess_lowercase not in ascii_lowercase):
            user_guess = input("The character you input is not a letter." +
                               "Please guess a letter: ")
            user_guess_lowercase = str(user_guess.lower())
        # Error handling: triggers a message if the user enters an input that
        # he already entered before
        if user_guess_lowercase in lettersGuessed:
            print("Oops! You've already guessed that letter: " +
                  getGuessedWord(secretWord, lettersGuessed) +
                  "\n" + "-------------")
            continue
        # Add the valid guess to the lettersGuessed list
        lettersGuessed.append(user_guess_lowercase)
        # Check if the guess is correct
        if user_guess_lowercase in secretWord:
            print("Good guess: " +
                  getGuessedWord(secretWord, lettersGuessed) +
                  "\n" + "-------------")
        else:
            # Reduce the remaining guesses by 1, since the guess was wrong
            guesses_left -= 1
            print("Oops! That letter is not in my word: " +
                  getGuessedWord(secretWord, lettersGuessed) +
                  "\n" + "-------------")


hangman(secretWord)
