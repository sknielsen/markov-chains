"""Generate markov text from text files."""


# add character limit to the resulting text (perhaps 140 char) AND end on
# a word!  And th 140 char limit ends on !?. punctuation.
# error check to make sure n_gram_length is an integer
#

from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open file and put it in one long string
    text_string = open(file_path).read()

    return text_string

def make_chains(text_string, n_gram_length):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """
    #create dictionary to hold result
    chains = {}
    n_gram_length = int(n_gram_length)
    #create variable to hold the words
    words = text_string.split()

    #look through words to find the word pairs that will be keys
    for i in range(len(words) - n_gram_length):
        key = ()
        for num in range(n_gram_length):
            key += (words[i + num],)

    #here is a successful way to do it, but below using setdefault is better
    #     if key in chains:
    #         chains[key].append(words[i+n_gram_length])
    #     else:
    #         chains[key] = [words[i+n_gram_length]]

        chains.setdefault(key, []).append(words[i+n_gram_length])
    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # your code goes here
    #pick a random key to start with
    #force only start on capital letter
    link_text = choice(chains.keys())
    while not link_text[0][0].isupper():
        link_text = choice(chains.keys())

    #this might work, but looking and then stopping is better
    # while True:
    #     try:
    #         new_link = (link_text[1], next_word)

    #     except KeyError:
    #         break
    #add our link text to the list
    link_text_list = list(link_text)
    words.extend(link_text_list)

    #look through to get random next word
    while link_text in chains:
        next_word = choice(chains[link_text])

        #add the new words to the string
        words.append(next_word)

        link_text = link_text[1:] + (next_word,)

    return " ".join(words)


def limit_to_140_char(string):
    """Take string and truncate to 140 characters

    Take string and limit to max 140 characters and end on punctuation
    """

    #truncate the string to 140 characters
    truncated_string = string[:140]

    #iterate backwards through the string until we find the index of !.?
    for i in range((len(truncated_string) - 1), 0, -1):
        if truncated_string[i] in ['.', '!', '?']:
            final_string = truncated_string[:(i + 1)]
            return final_string
        #if
    for i in range((len(truncated_string) - 1), 0, -1):
        if truncated_string[i] == ',':
            final_string = truncated_string[:(i + 1)]
            return final_string

    for i in range((len(truncated_string) - 1), 0, -1):
        if truncated_string[i] == ' ':
            final_string = truncated_string[:(i + 1)]
            return final_string
    #slice the string from begining to that index +1




#input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text, sys.argv[2])

# Produce random text
random_text = make_text(chains)

# Check if text is great than 140 characters
if len(random_text) > 140:
    random_text = limit_to_140_char(random_text)

print random_text
