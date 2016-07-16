import random

#write a function to get a list and a random word if level is easy
def easy_words(word_list):
    my_easy_list = []
    #with open('/usr/share/dict/words', 'r') as f:
    for item in word_list:
        if len(item.strip()) >= 4 and len(item.strip()) <= 6:
            my_easy_list.append(item.strip())
    return my_easy_list
    #print(my_easy_list)

#write a function to get a list and a random word if level is normal
def medium_words(word_list):
    my_normal_list = []
    #with open('/usr/share/dict/words', 'r') as f:
    for item in word_list:
        if len(item.strip()) >= 6 and len(item.strip()) <= 8:
            my_normal_list.append(item.strip())
    return my_normal_list
    #print(my_normal_list)

#write a function to get a list and a random word if level is hard
def hard_words(word_list):
    my_hard_list = []
    #with open('/usr/share/dict/words', 'r') as f:
    for item in word_list:
        if len(item.strip()) >= 8:
            my_hard_list.append(item.strip())
    return my_hard_list
    #print(my_hard_list)

#write a function that asks user to choose a level of difficulty
def random_word(word_list, level):
    filtered_word_list = []
    my_word = ""

    if level == "easy":
        filtered_word_list = easy_words(word_list)
        my_word = random.choice(filtered_word_list)

    elif level == "normal":
        filtered_word_list = medium_words(word_list)
        my_word = random.choice(filtered_word_list)

    elif level == "hard":
        filtered_word_list = hard_words(word_list)
        my_word = random.choice(filtered_word_list)

    print(my_word)
    print(" _ " * len(my_word))
    return my_word

#write a function to guess a word
#def display_word(word, guesses):

def main():
    level = input("Please enter the level of difficulty: ").lower()

    with open('/usr/share/dict/words', 'r') as word_list:
        random_word(word_list, level)

if __name__ == '__main__':
    main()
