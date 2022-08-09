import random
wordlist = ["python", "java", "swift", "javascript"]  # preset list of words
messages = ["attempt", "attempts", "Input a letter:", "That letter doesn't appear in the word.", "No improvements.", "Please, input a single letter.", "Please, enter a lowercase letter from the English alphabet.", "You've already guessed this letter.", "You guessed the word ", "You survived!", "You lost!", "Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:", "You won: ", "You lost: ", "times"]
start_game = 1  # start flag to be set later when menu loop is added
att = 8  # number of attempts per game
letters_tried = []  # list of letters tried by player
letters_found = []  # list of letters tried by player and appearing in word
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 'r', "s", "t", "u", "v", "w", "x", "y", "z"]
commands = ["play", "results", "exit"]  # menu commands
win_counter = 0  # counter for times won
lost_counter = 0  # counter for times lost
# set_letters_found - letters_found as a set for comparison with correct_letters
# mystery_word - word chosen by computer for a particular round of game
# word_by_letter = []  - list of letters in mystery word
# set_correct_letters - mystery word as a set of letters for comparison with set_letters_found
# alef - initial input by player
# bet - input checked for errors - see tasks for stage 7/8 of project
print("H A N G M A N  # 8 attempts")


def menu():
    while True:
        option = input(messages[11])
        if option not in commands:
            continue
        elif option == "play":
            run_game()
            break
        elif option == "results":
            print(messages[12], win_counter, messages[14])
            print(messages[13], lost_counter, messages[14])
            continue
        elif option == "exit":
            break


def setup_word():
    global mystery_word
    global word_by_letter
    global camo_word  # list where letters are replaced by "-" signs
    global set_correct_letters
    global letters_tried
    global letters_found
    mystery_word = random.choice(wordlist)
    theta = len(mystery_word)  # length of mystery word
    camo_word = "-" * theta
    word_by_letter = list(mystery_word)
    set_correct_letters = set()
    set_correct_letters.update(mystery_word)
    letters_tried.clear()  # clear letters tried in previous game round
    letters_found.clear()  # clear letters found in previous game round
    # print(word_by_letter, "word_by_letter printed check word as list")  # check line remove for submission
    # print(camo_word, "check camo word")  # check line remove for submission
    return camo_word


def take_and_check_input():
    global bet
    while True:
        alef = input(messages[2])
        if len(alef) != 1:
            print(messages[5])
            print()
            print("".join(camo_word))
        elif alef not in alphabet:
            print(messages[6])
            print()
            print("".join(camo_word))
        elif alef in letters_tried:
            print(messages[7])
            print()
            print("".join(camo_word))
        else:
            bet = alef
            break


def play():
    global att
    global camo_word
    global letters_found
    global letters_tried
    global win_counter
    global lost_counter
    while att > 0:
        set_letters_found = set(letters_found)
        if set_letters_found == set_correct_letters:
            win_counter += 1
            print()
            print(messages[8] + mystery_word + "!")
            print(messages[9])
            menu()
            break
        else:
            print()
            print("".join(camo_word))
            take_and_check_input()
            if bet not in word_by_letter:
                att -= 1  # attempts / lives deducted here to modify later see tasks for stage 6/8 of project
                letters_tried.append(bet)  # add bet to tried letters for further use in checking tried letters - see tasks for stage 7/8 of project
                if att != 1:
                    print(messages[3])
                    print("#", att, "attempts")
                else:
                    print(messages[3])
                    print("# 1 attempt")
            else:
                letters_found.append(bet)  # add bet to found letters for further use in checking tried letters - see tasks for stage 7/8 of project
                letters_tried.append(bet)  # add bet to tried letters for further use in checking tried letters - see tasks for stage 7/8 of project
                alpha = mystery_word.find(bet)
                omega = mystery_word.rfind(bet)
                found_places = []
                found_places.append(alpha)
                if omega != -1:
                    found_places.append(omega)
                camo_word = [bet if idx in found_places else ele for idx, ele in enumerate(camo_word)]
                continue
    if att == 0:
        lost_counter += 1
        print("".join(camo_word))
        print()
        print(messages[10])
        menu()


def run_game():
    setup_word()
    play()


menu()
