from project import check_status, render_hidden_word, draw_hangman

def main():
    test_check_status_1()
    test_check_status_2()
    test_check_status_3()
    test_draw_hangman_1()
    test_render_hidden_word_1()

def test_check_status_1():
    characters = ['a', 'b']
    h_word_characters = ['a','b']
    turn = 5
    word = "xy"
    assert check_status(characters, h_word_characters, turn, word) == True

def test_check_status_2():
    characters = ['a', 'b']
    h_word_characters = ['c','d']
    turn = 0
    word = "xy"
    assert check_status(characters, h_word_characters, turn, word) == True

def test_check_status_3():
    characters = ['a', 'b']
    h_word_characters = ['c','d']
    turn = 5
    word = "xy"
    assert check_status(characters, h_word_characters, turn, word) == False

def test_draw_hangman_1(capfd):
    turn = 6
    draw_hangman(turn)
    out, err = capfd.readouterr()
    assert out == "=========\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n"

def test_render_hidden_word_1():
    word = "testwORD"
    assert render_hidden_word(word) == "********"

if __name__ == "__main__":
    main()
