"""
feed the file in and get out all the text as a string

take that string
    1) get out a string of all the characters
    2) get out one string for each character of all their lines

all_characters string -> make_chains produces a dictionary for who talks to whom

each character_lines -> make_chains produces a dictionary for each character of what they say

"""

import markov
import re

#open the script and put it all in one string
script_text = markov.open_and_read_file(["friends.txt"])

#edit the script to remove things that we don't want to deal with
clean_script_text = re.sub(r'\([^)]+\)', '', script_text)
