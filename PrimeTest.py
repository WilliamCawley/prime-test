#!/usr/bin/env python

"""PrimeTest.py - Processes a provided list of words and then searches this for an anagram provided by the user"""

DATA = """\
starlet
startle
reduces
rescued
realist
recused
saltier
retails
secured
"""
# The below constant contains the letters of the English language sorted by frequency
FREQUENCY_SORTED_LETTERS = "etaoinsrhdlucmfywgpbvkxqjz"
# The below constant contains the first 26 prime numbers to match to FREQUENCY_SORTED_LETTERS
PRIME_NUMBERS = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def process(reference):
    """Takes in the word data provided (reference) and processes it ready for use in searching for anagrams"""
    reference.lower()
    # Create a map of letters to prime numbers based on the frequency of letters in the English language
    letter_to_prime = {}
    for i in range(len(
            PRIME_NUMBERS)):
        letter_to_prime[FREQUENCY_SORTED_LETTERS[i]] = PRIME_NUMBERS[i]

    word_hash_values = []
    for line in reference.splitlines():
        hash_value = 1
        # The loop below will calculate the hash value of each word.
        # This is achieved by multiplying the prime number value of the letters.
        # The hash value of a word always stays the same even if the letters are in a different order
        for letter in line:
            if letter in letter_to_prime:
                hash_value *= letter_to_prime[letter]
        word_hash_values.append([line, hash_value])  # Add the line and hash value to an array
    return [letter_to_prime, word_hash_values]


# Calculate the provided anagram hash value, and compare with previously processed results
def find_anagrams(word_hash_values, letter_to_prime, word):
    """Using parameters from the 'process' function, this will search the data provided earlier for the anagram"""
    hash_index = 1
    final_string = ''
    for letter in word:
        if letter in letter_to_prime:
            hash_index *= letter_to_prime[letter]
    for word_hash in word_hash_values:
        if hash_index == word_hash[1]:
            if word_hash[0] in word:  # Ensure I don't display the original provided anagram
                continue
            final_string = final_string + word_hash[0] + "\n"
            continue
        else:
            continue
    if final_string:
        return final_string
    else:
        return False


anagram_params = process(DATA)
results = find_anagrams(anagram_params[1], anagram_params[0], word="rescued")
print(results)

# NOTES:
#
# There are a few things missing that I feel would take a disproportionate amount of time to include considering this is
# the first stage of an interview yet I haven't spoken to anyone from the organisation.
#
# 1. A proper input method for 10.000.000 words, for example reading in from a txt, json etc
# 2. Error handling with informative messages
# 3. Further scenarios for special characters and apostrophes

__author__ = "William Cawley"
__copyright__ = "NA"
__version__ = "1.0.0"
__maintainer__ = "William Cawley"
__email__ = "willjcawley@gmail.com"
__status__ = "Development"
