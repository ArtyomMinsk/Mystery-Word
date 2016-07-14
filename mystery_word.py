import random

#write a function that asks user to choose a level of difficulty
def level_of_difficulty():
    level = input("Please enter the level of difficulty: ").lower()
    if level == "easy":
        print("You chose an easy level!")
        return get_easy_list()
    elif level == "normal":
        print("You chose a normal level!")
        return get_normal_list()
    elif level == "hard":
        print("You chose a hard level!")
        return get_hard_list()

    # secret_word = random.choice(my_word_list)
    # print("Your secret word is: ", secret_word)

#write a function to get a list if level is easy
def get_easy_list():
    my_easy_list = []
    with open('/usr/share/dict/words', 'r') as f:
    #my_word_list = ["art", "shannon", "robert", "michael", "tommy", "nesterenko", "sergeevich"]
        for item in f:
            if len(item) >= 4 and len(item) <= 6:
                my_easy_list.append(item)

    print(my_easy_list)

#write a function to get a list if level is normal
def get_normal_list():
    my_normal_list = []
    with open('/usr/share/dict/words', 'r') as f:
    #my_word_list = ["art", "shannon", "robert", "michael", "tommy", "nesterenko", "sergeevich"]
        for item in f:
            if len(item) >= 6 and len(item) <= 8:
                my_normal_list.append(item)

    print(my_normal_list)

#write a function to get a list if level is hard
def get_hard_list():
    my_hard_list = []
    with open('/usr/share/dict/words', 'r') as f:
    #my_word_list = ["art", "shannon", "robert", "michael", "tommy", "nesterenko", "sergeevich"]
        for item in f:
            if len(item) >= 8:
                my_hard_list.append(item)

    print(my_hard_list)

level_of_difficulty()
