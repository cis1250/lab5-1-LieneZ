#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

# This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

def get_sentence():
    user_sentence = input("Enter a sentence: ")

    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")

    return user_sentence


def calculate_frequencies(sentence):
    words = []
    frequencies = []

    for w in sentence:
        w = w.lower()
        w = w.rstrip("!,?.:;")
        if w not in words:
            words.append(w)
            frequencies.append(1)
        else:
            frequencies[words.index(w)] += 1

    print_frequencies(words, frequencies)


def print_frequencies(words, frequencies):
    for i in range(0, len(words)):
        print(words[i], ": ", frequencies[i], sep='')



def main():

    sentence = get_sentence()
    sentence = sentence.split()

    calculate_frequencies(sentence)


if __name__ == "__main__":
        main()

