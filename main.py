# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    first_word = word
    second_word = anagram
    if sorted(first_word) != sorted(second_word):
        return False
    else:
        return True
