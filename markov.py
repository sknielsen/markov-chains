"""Generate markov text from text files."""


# add character limit to the resulting text (perhaps 140 char) AND end on
# a word!  And th 140 char limit ends on !?. punctuation.
# error check to make sure n_gram_length is an integer
#

from random import choice
import sys


def open_and_read_file(files):
    """Takes file path as string; returns text as string.

    >>> open_and_read_file(['green-eggs.txt'])
    'Would you could you in a house?\\nWould you could you with a mouse?\\nWould you could you in a box?\\nWould you could you with a fox?\\nWould you like green eggs and ham?\\nWould you like them, Sam I am?\\n'

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open any number of files and put them in one long string
    text_string = ''

    for text_file in files:
        text_string += open(text_file).read()

    return text_string


def make_chains(text_string, n_gram_length):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:
    >>> make_chains('Would you could you in a house?\\nWould you could you with a mouse?\\nWould you could you in a box?\\nWould you could you with a fox?\\nWould you like green eggs and ham?\\nWould you like them, Sam I am?\\n', 2)
    {('a', 'fox?'): ['Would'], ('Sam', 'I'): ['am?'], ('could', 'you'): ['in', 'with', 'in', 'with'], ('you', 'with'): ['a', 'a'], ('box?', 'Would'): ['you'], ('ham?', 'Would'): ['you'], ('you', 'in'): ['a', 'a'], ('a', 'house?'): ['Would'], ('like', 'green'): ['eggs'], ('like', 'them,'): ['Sam'], ('and', 'ham?'): ['Would'], ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'], ('you', 'could'): ['you', 'you', 'you', 'you'], ('a', 'mouse?'): ['Would'], ('them,', 'Sam'): ['I'], ('in', 'a'): ['house?', 'box?'], ('with', 'a'): ['mouse?', 'fox?'], ('house?', 'Would'): ['you'], ('a', 'box?'): ['Would'], ('green', 'eggs'): ['and'], ('you', 'like'): ['green', 'them,'], ('mouse?', 'Would'): ['you'], ('fox?', 'Would'): ['you'], ('eggs', 'and'): ['ham?']}

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
        chains.setdefault(key, []).append(words[i+n_gram_length])

    return chains


def make_text(chains):
    """Returns text from chains.

    >>> text_test = make_text({('a', 'fox?'): ['Would'], ('Sam', 'I'): ['am?'], ('could', 'you'): ['in', 'with', 'in', 'with'], ('you', 'with'): ['a', 'a'], ('box?', 'Would'): ['you'], ('ham?', 'Would'): ['you'], ('you', 'in'): ['a', 'a'], ('a', 'house?'): ['Would'], ('like', 'green'): ['eggs'], ('like', 'them,'): ['Sam'], ('and', 'ham?'): ['Would'], ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'], ('you', 'could'): ['you', 'you', 'you', 'you'], ('a', 'mouse?'): ['Would'], ('them,', 'Sam'): ['I'], ('in', 'a'): ['house?', 'box?'], ('with', 'a'): ['mouse?', 'fox?'], ('house?', 'Would'): ['you'], ('a', 'box?'): ['Would'], ('green', 'eggs'): ['and'], ('you', 'like'): ['green', 'them,'], ('mouse?', 'Would'): ['you'], ('fox?', 'Would'): ['you'], ('eggs', 'and'): ['ham?']})
    >>> text_test[0].isupper()
    True
    """

    words = []

    # your code goes here
    #pick a random key to start with
    link_text = choice(chains.keys())

    #force only start on capital letter
    while not link_text[0][0].isupper():
        link_text = choice(chains.keys())

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

    >>> test_length = limit_to_140_char('Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we here highly resolve that these dead shall not perish from the earth.')
    >>> len(test_length) <= 140
    True

    """

    #truncate the string to 140 characters
    truncated_string = string[:140]

    #iterate backwards through the string until we find the index of !.?
    for i in range((len(truncated_string) - 1), 0, -1):
        if truncated_string[i] in ['.', '!', '?']:
            #slice the string from begining to that index +1
            final_string = truncated_string[:(i + 1)]
            return final_string

    #repeat for if there is no .!? and add elipses to make it look nice
    for i in range((len(truncated_string) - 3), 0, -1):
        if truncated_string[i] in [',', ' ']:
            final_string = truncated_string[:i] + '...'
            return final_string

def main():
    # Open the files and turn them into one long string
    input_text = open_and_read_file(sys.argv[1:-1])

    # Check for valid integer for n gram length
    try:
        # Get a Markov chain
        chains = make_chains(input_text, sys.argv[-1])
        # Produce random text
        random_text = make_text(chains)

        # Check if text is great than 140 characters
        if len(random_text) > 140:
            random_text = limit_to_140_char(random_text)

        print random_text
    except ValueError:
        print "Please give a valid integer for the n-gram length"

#for testing
if __name__ == "__main__":
    main()
    # import doctest
    # result = doctest.testmod()
    # if result.failed == 0:
    #     print("ALL TESTS PASSED")
