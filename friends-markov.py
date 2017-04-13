"""
feed the file in and get out all the text as a string

take that string
    1) get out a string of all the characters
    2) get out one string for each character of all their lines

all_characters string -> make_chains produces a dictionary for who talks to whom

each character_lines -> make_chains produces a dictionary for each character of what they say

script found at: http://uncutfriendsepisodes.tripod.com/season1/103uncut.htm
"""

import markov
import re
import pprint


def make_character_lines(character_name, text_string):
    """Given character name and the text, returns a markov dictionary of their lines from text"""

    characters_lines = re.findall('(?<=' + re.escape(character_name) + '\ )[\s\S]+?(?=\n\n)', text_string)
    characters_lines = ' '.join(characters_lines)
    characters_markov = markov.make_chains(characters_lines, '2')
    return characters_markov


#open the script and put it all in one string
script_text = markov.open_and_read_file(["friends.txt"])

#edit the script to remove things that we don't want to deal with
clean_script_text = re.sub(r'\([^)]+\)', '', script_text)
clean_script_text = re.sub(r'\[[^\]]+\]', '', clean_script_text)

#find the character names and put them in a list
characters_list = re.findall('[A-Z]\w+\:', clean_script_text)

#take the list and convert it to a text string
characters = ' '.join(characters_list)
#create markov dictionary from characters string
character_markov = markov.make_chains(characters, '2')

# Create dictionary with character names and their markov chains
character_lines_markov = {}
for character in set(characters_list):
    character_lines_markov[character] = make_character_lines(character, clean_script_text)

print pprint.pprint(character_lines_markov)

#for testing
#print character_markov
#print make_character_lines('Rachel:', clean_script_text)
