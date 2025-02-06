import random


def random_word():
    list_word = []
    with open("sowpods.txt", "r") as f:
        line = f.readline().strip()
        list_word.append(line)
        while line:
            # do something to the line, for example
            # saving it to disk
            line = f.readline().strip()
            list_word.append(line)

    random_word_index = random.randint(0, len(list_word))

    print(list_word[random_word_index])


random_word()
