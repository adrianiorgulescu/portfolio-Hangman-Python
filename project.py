import helpers

def main():

    #Initialise the working directory:
    fileDir = helpers.set_working_dir()
    
    #Print hello text and game rules on screen. Use a text file.
    helpers.clear_terminal() #Clear the terminal initially

    #Show hello message on screen
    helpers.open_hello()
    
    #allow user to choose a category of words to play
    category, categories = helpers.choose_category()

    #generate a random word from the chosen category
    word = helpers.generate_word(category).upper()

    #draw the hangman for the start of the game
    helpers.clear_terminal()
    helpers.draw_hangman(10, fileDir)

    #inform user of the category chosen (display on screen)
    helpers.show_chosen_category(category, categories)
    
    #render the word(hidden characters) on screen
    hidden_word = helpers.render_hidden_word(word)

    #start the guessing of characters until game is won or lost
    helpers.guess(word, hidden_word, fileDir)

if __name__ == "__main__":
    main()
