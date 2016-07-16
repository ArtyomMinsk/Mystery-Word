def display_word(word, guesses):
    secret_word_list = list(word)
    print(secret_word_list)
    print("Letters guessed list: {}".format(guesses))

    guessed_word_list = []
    for letter in range(len(secret_word_list)):
        guessed_word_list.append("_")
    #print(guessed_word_list)

    for letter in guesses:
        for index in range(len(secret_word_list)):
            if letter == secret_word_list[index]:
                guessed_word_list.insert(index, letter)
                guessed_word_list.pop(index + 1)

    display = (' '.join(guessed_word_list)).upper()
    print(display)
    return display

def is_word_complete(word, guesses):
    secret_word_list = list(word)
    print(secret_word_list)
    print("Letters guessed list: {}".format(guesses))

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
        print("Yes")
        return True
    else:
        print("No")
        return False

def guess_a_word():
    # secret word and list representation
    secret_word = "nesterenko"
    secret_word_list = list(secret_word)
    print("Secret word is: ", secret_word_list)

    # list displaying the currently guessed word, with _
    guessed_word_list = []

    # list of all previously guessed letters
    letters_guessed_list = []

    # number of incorrect guesses, maximum of 8
    guess = 0

    # make a list of _ with length of secret_word
    length = len(secret_word_list)
    for letter in range(length):
        guessed_word_list.append("_")
    print(guessed_word_list)

    while True:
        if guess < 8 and guessed_word_list == secret_word_list:
            print("Congratulations! You guessed the word!")
            #return True
            break

        elif guess == 8 and guessed_word_list != secret_word_list:
            print("You lost!")
            #return True
            break

        input_letter = input("Please guess a letter: ").lower()

        #check if user guessed a letter before
        if input_letter in letters_guessed_list:
            print("You have already guessed this letter! ")
            continue
        else:
            letters_guessed_list.append(input_letter)
            print("Letters guessed list: {}".format(letters_guessed_list))

        # display_word(secret_word, letters_guessed_list)

        #check if user guessed a letter
        in_list = False
        for letter in range(length):
            #guessed_word_list.append("_")
            if input_letter == secret_word_list[letter]:
                guessed_word_list.insert(letter, input_letter)
                guessed_word_list.pop(letter + 1)
                #guessed_word_list.append("_")
                in_list = True

        print("The updated guessed word is:\n {}".format(guessed_word_list))
                #length -= 1

        if in_list == True:
            print("You guessed a letter!")
        else:
            print("You didn't guess a letter!")
            guess += 1

        print("You have {} guesses left".format(8 - guess))

#guess_a_word()
var_word = list("nestrnko")
is_word_complete("nesterenko", var_word)
# [_,_,_]
