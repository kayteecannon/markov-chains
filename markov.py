"""Generate Markov text from text files."""

from random import choice

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents = open(file_path).read()

    return contents


text_content = open_and_read_file('green-eggs.txt')


def make_chains(text_string=text_content):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    word_list = text_string.split()

    for i in range(len(word_list) - 2):
        key = (word_list[i], word_list[i + 1])
        value = word_list[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


# print(make_chains(text_content))


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    current_key = random.choice(list(chains))
    words = [current_key[0], current_key[1]]
    current_value = random.choice(chains[current_key])

    while current_key is not None:
        words.append(current_value)

        current_key = (current_key[1], current_value)
        if current_key == ('I', 'am?'):
            break
        current_value = random.choice(chains[current_key])

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
