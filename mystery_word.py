import random

#write a function that asks user to choose a level of difficulty
def get_secret_word():
    level = input("Please enter the level of difficulty: ").lower()
    if level == "easy":
        print("You chose an easy level!")
        my_easy_list = get_easy_list()

        my_word = random.choice(my_easy_list)
        print(my_word)
        print(" _ " * len(my_word))
        return my_word

    elif level == "normal":
        print("You chose a normal level!")
        my_normal_list = get_normal_list()

        my_word = random.choice(my_normal_list)
        print(my_word)
        print(" _ " * len(my_word))
        return my_word

    elif level == "hard":
        print("You chose a hard level!")
        my_hard_list = get_hard_list()

        my_word = random.choice(my_hard_list)
        print(my_word)
        print(" _ " * len(my_word))
        return my_word

#write a function to get a list and a random word if level is easy
def get_easy_list():
    my_easy_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for item in f:
            if len(item.strip()) >= 4 and len(item.strip()) <= 6:
                my_easy_list.append(item.strip())
    return my_easy_list


#write a function to get a list and a random word if level is normal
def get_normal_list():
    my_normal_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for item in f:
            if len(item.strip()) >= 6 and len(item.strip()) <= 8:
                my_normal_list.append(item.strip())
    return my_normal_list


#write a function to get a list and a random word if level is hard
def get_hard_list():
    my_hard_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for item in f:
            if len(item.strip()) >= 8:
                my_hard_list.append(item.strip())
    return my_hard_list


get_secret_word()
