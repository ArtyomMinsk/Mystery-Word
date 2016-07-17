import random
#level = ""

# Write a function to get a list and a random word if level is easy
def easy_words(word_list):
    my_easy_list = []
    #with open('/usr/share/dict/words', 'r') as f:
    for item in word_list:
        if len(item.strip()) >= 4 and len(item.strip()) <= 6:
            my_easy_list.append(item.strip())
    return my_easy_list
    #print(my_easy_list)

# Write a function to get a list and a random word if level is normal
def medium_words(word_list):
    my_normal_list = []
    #with open('/usr/share/dict/words', 'r') as f:
    for item in word_list:
        if len(item.strip()) >= 6 and len(item.strip()) <= 8:
            my_normal_list.append(item.strip())
    return my_normal_list
    #print(my_normal_list)

# Write a function to get a list and a random word if level is hard
def hard_words(word_list):
    my_hard_list = []
    #with open('/usr/share/dict/words', 'r') as f:
    for item in word_list:
        if len(item.strip()) >= 8:
            my_hard_list.append(item.strip())
    return my_hard_list
    #print(my_hard_list)

# Return a random word from the easy/normal/hard list
def random_word(word_list):
    my_word = ""
    my_word = random.choice(word_list)
    return my_word

# Return a string that including blanks (_) and letters from the given word
def display_word(word, guesses):
    secret_word_list = list(word)
    #print(secret_word_list)
    #print("Letters guessed list: {}".format(guesses))

    guessed_word_list = []
    for letter in range(len(secret_word_list)):
        guessed_word_list.append("_")
    #print(guessed_word_list)
    in_list = False
    for letter in guesses:
        for index in range(len(secret_word_list)):
            if letter == secret_word_list[index]:
                guessed_word_list.insert(index, letter)
                guessed_word_list.pop(index + 1)
                in_list = True

    display = (' '.join(guessed_word_list)).upper()
    print(display)
    return display

# Returns True if the list of guesses covers every letter in the word,
# otherwise returns False
def is_word_complete(word, guesses):
    secret_word_list = list(word)
    #print(secret_word_list)
    #print("Letters guessed list: {}".format(guesses))

    guessed_word_list = []
    for letter in range(len(secret_word_list)):
        guessed_word_list.append("_")

    for letter in guesses:
        for index in range(len(secret_word_list)):
            if letter == secret_word_list[index]:
                guessed_word_list.insert(index, letter)
                guessed_word_list.pop(index + 1)

    display = ''.join(guessed_word_list)
    if word == display:
        print(' '.join(display.upper()))
        return True
    else:
        return False

def main():
    while True:
        # Prompt the user for a difficulty level
        level = input("Please enter the level of difficulty (easy/normal/hard): ").lower()
        short_list = []

        # Set up the game based upon the difficulty level
        with open('/usr/share/dict/words', 'r') as word_list:
            if level == "easy":
                short_list = easy_words(word_list)

            elif level == "normal":
                short_list = medium_words(word_list)

            elif level == "hard":
                short_list = hard_words(word_list)

            word = random_word(short_list).lower()
            #print(word)

        secret_word_list = list(word)

        # The number of quesses
        guess = 0

        # This list stores all previous guesses
        letters_guessed_list = []

        # Perform the game loop
        while True:
            # Display whether the user has won or lost
            if guess < 8 and is_word_complete(word, letters_guessed_list):
                print("Congratulations! You guessed the word!")
                # Give the user the option to play again
                answer = input("Would you like to play again? [Y/n] ").lower()
                break

            elif guess == 8 and not is_word_complete(word, letters_guessed_list):
                print("You lost!")
                print("The secret word was: ", word.upper())
                # Give the user the option to play again
                answer = input("Would you like to play again? [Y/n] ").lower()
                break

            # Print the number of guesses remaining
            print("You have {} guesses left".format(8 - guess))

            display_word(word, letters_guessed_list)

            # Prompt the user for a letter to guess
            input_letter = input("Please guess a letter: ").lower()

            # Check for invalid input
            if len(input_letter) > 1:
                print("The input is invalid! Please try again!")
                input_letter = input("Please guess a letter: ").lower()

            # Check if user guessed a letter before
            if input_letter in letters_guessed_list:
                print("You have already guessed this letter! Please try again! ")
                continue
            else:
                # Print the letters that have been guessed so far
                letters_guessed_list.append(input_letter)
                print("Letters that have been guessed so far: {}".format(letters_guessed_list))

            if input_letter not in secret_word_list:
                 guess += 1

        if answer == "y":
            continue
        elif answer == "n":
            break

if __name__ == '__main__':
    main()
