import random

#write a function that asks user to choose a level of difficulty
def level_of_difficulty():
    level = input("Please enter the level of difficulty: ").lower()
    if level == "easy":
        print("You chose an easy level!")
        return get_easy_word()
    elif level == "normal":
        print("You chose a normal level!")
        return get_normal_word()
    elif level == "hard":
        print("You chose a hard level!")
        return get_hard_word()

#write a function to get a list and a random word if level is easy
def get_easy_word():
    my_easy_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for item in f:
            if len(item.strip()) >= 4 and len(item.strip()) <= 6:
                my_easy_list.append(item.strip())
    my_word = random.choice(my_easy_list)
    print(my_word)
    print(" _ " * len(my_word))
    return random.choice(my_easy_list)

#write a function to get a list and a random word if level is normal
def get_normal_word():
    my_normal_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for item in f:
            if len(item.strip()) >= 6 and len(item.strip()) <= 8:
                my_normal_list.append(item.strip())
    my_word = random.choice(my_normal_list)
    print(my_word)
    print(" _ " * len(my_word))
    return random.choice(my_normal_list)

#write a function to get a list and a random word if level is hard
def get_hard_word():
    my_hard_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for item in f:
            if len(item.strip()) >= 8:
                my_hard_list.append(item.strip())
    my_word = random.choice(my_hard_list)
    print(my_word)
    print(" _ " * len(my_word))
    return random.choice(my_hard_list)

level_of_difficulty()
