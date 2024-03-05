import sys
import random
import csv
import os
from pyfiglet import Figlet


def main():

    #Initialise the working directory:
    workingDir = os.getcwd()
    fileDir = workingDir + '\hangman_ascii'

    #Print hello text and game rules on screen. Use a text file.
    clear_terminal() #Clear the terminal initially
    try:
        with open("Hello.txt", "r") as file:
            hello = file.read()
            print (f"{hello}")
    except FileNotFoundError:
        sys.exit("Hello file not present. Can't start the game.")

    #allow user to choose a category of words to play
    category, categories = choose_category()

    #generate a random word from the chosen category
    word = generate_word(category).upper()

    #draw the hangman for the start of the game
    clear_terminal()
    draw_hangman(10, fileDir)

    #inform user of the category chosen
    for keys, value in categories.items():
        if str(value) == category:
            print(f"You have chosen category {keys}: {value}.\n")

    #render the word(hidden characters) on screen
    hidden_word = render_hidden_word(word)

    #start the guessing of characters
    guess(word, hidden_word, fileDir)

def choose_category():
    #define categories and list them on screen
    categories = {1:'Animals',2:'Flowers',3:'Countries',4:'Birds',5:'Names'}
    print("")
    print("Available categories:")
    for keys, value in categories.items():
        print(keys, value)

    #allow user to select category. accept only valid answers and ask until valid ans is received
    #then return category
    while True:
            category = input("Please select a category (1, 2, 3, 4 or 5): \n")
            if category not in ["1","2","3","4","5"]:
                continue
            else:
                for keys, value in categories.items():
                    if str(keys) == category:
                        category = value
                  #      clear_terminal()
                  #      print(f"You have chosen category {keys}: {value}.\n")
                return category, categories

def generate_word(category):
    # Reader: read the category data in the csv file and create a list for the current cat
    #return a random word from the list
    list = []
    try:
        with open("categories.csv", "r", encoding = 'cp850') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row[category] != "":
                    list.append(row[category])
            return random.choice(list)
    except FileNotFoundError:
        sys.exit("categories csv file does not exist")

def guess(word, hidden_word, fileDir):
    #initialize empty lists to receive individual characters
    characters = []
    used = []
    valid = []
    h_word_characters = []

    #initialize the turn equal to 10:
    turn = 10

    #add characters to the empty lists
    for i in range (len(word)):
        c = word[i]
        characters.append(c)

    for i in range (len(hidden_word)):
        c = hidden_word[i]
        h_word_characters.append(c)

    #ask for input from user
    #ask input until the game is lost or won
    #call the 'check_status' function to see if won or lost
    while len(characters) > 0:
        guess = input("Please enter your guess: ").upper()
        used.append(guess)

        # Add code here to ensure that the guess is a single character a-z, ', -,  or space.
        if guess in characters:
            clear_terminal()
            if turn < 11:
                draw_hangman(turn, fileDir)
            valid.append(guess)

        else:
            clear_terminal()
            turn -= 1
            draw_hangman(turn, fileDir)

        #show on screen which character the user typed already
        print(f"Characters used: {used}\n")

        #show the word on screen, hiding characters that have not been guessed already
        h_word_characters = render_word(h_word_characters, valid, characters)

        #check if win or lose.
        #if either of these, break. If false, continue with the loop
        if check_status(characters, h_word_characters, turn, word, fileDir):
            break 
        else:
            continue

def draw_hangman(turn, fileDir):
    #go to the folder where the hangman ascii is saved
    os.chdir(fileDir)

    #get the current hangman ascii and print it on screen
    hang_file_name = str(turn) + " hangman ascii.txt"
    try:
        with open(hang_file_name, "r") as file:
            reader = file.read()
            print (reader)
    except FileNotFoundError:
        sys.exit("Hangman file not found. Game can't continue!")

def render_word(h_word_characters, valid, characters):
    #render the word with hidden characters and guessed characters
    for i in range(len(characters)):
        if characters[i] in valid:
            h_word_characters[i] = characters[i]

    print("Your word is:\n")
    print(f"{''.join(h_word_characters)} out of {len(h_word_characters)} characters\n")
    return h_word_characters

def render_hidden_word(word):
    #render the whole word hidden. Only used initially.
    hidden_word = "*" * len(word)
    print("Your word is:\n")
    print(f"{hidden_word} out of {len(word)} characters\n")
    return hidden_word

def check_status(characters, h_word_characters, turn, word, fileDir):
    #use figlet for ascii art words and select font
    figlet = Figlet()
    font = "ogre"

    #check if won and if true, print congrats on screen, return true
    if turn > 0 and characters == h_word_characters:
        print_won_on_screen(h_word_characters, turn, fileDir, figlet, font)

    #check if lost and if true, print lost on screen, return true
    elif turn == 0:
        print_lost_on_screen(h_word_characters, turn, word, fileDir, figlet, font)

    #if not lost or won return false
    else:
        return False

def print_lost_on_screen(h_word_characters, turn, word, fileDir, figlet, font):
    clear_terminal()
    draw_hangman(turn, fileDir)
    print(f"{''.join(h_word_characters)} out of {len(h_word_characters)} characters\n")
    print(f"The word is: {word}\n")
    text = "You lost!\nTry again!"
    figlet.setFont(font=font)
    print(figlet.renderText(text))
    sys. exit()

def print_won_on_screen(h_word_characters, turn, fileDir, figlet, font):
    clear_terminal()
    draw_hangman(turn, fileDir)
    print(f"{''.join(h_word_characters)} out of {len(h_word_characters)} characters\n")
    text = "Congrats!\nYou won!"
    figlet.setFont(font=font)
    print(figlet.renderText(text))
    sys. exit()

def clear_terminal():
    #a function to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
