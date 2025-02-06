# Der Code liest Wörter aus der Datei sowpods.txt, speichert sie in einer Liste und gibt eines zufällig aus.

import random


def random_word():
    list_word = []
    with open("sowpods.txt", "r") as f:
        line = f.readline().strip()
        list_word.append(line)
        while line:
            line = f.readline().strip()
            list_word.append(line)

    random_word_index = random.randint(0, len(list_word) - 1)

    print(list_word[random_word_index])


random_word()
