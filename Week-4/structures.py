'''
structures.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list".
def first_and_last(the_list):
    """returns the first and last elements of the given list"""
    last = len(the_list)-1
    return [the_list[0], the_list[last]]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    """returns the given section of the list between beginning and end, in reverse order"""
    if end < beginning:
        raise ValueError
    if beginning < 0:
        raise ValueError
    if end > len(the_list):
        raise ValueError
    newlist = the_list[beginning:end]
    newlist.reverse()
    return newlist


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    """repeats the element of the list three times starting at the index of that element"""
    the_list.insert(index, the_list[index])
    the_list.insert(index, the_list[index])
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    """tests if a word is a palindrome (same backwards and fowards)"""
    word = word.lower()
    return word[::-1] == word

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    """tests if a sentence is a palindrome, ignoring punctuation and spaces"""
    sentence = sentence.lower()
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('.', '')
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('?', '')
    sentence = sentence.replace('!', '')
    return sentence[::-1] == sentence

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    """combines two sentences, given that they start with a capital and end with a period"""
    sentence1 = sentence1.strip()
    sentence1 = sentence1 + ' '
    sentence2 = sentence2.strip()
    if sentence1[0].isupper() and sentence1[len(sentence1)-2] == '.' and sentence2[0].isupper():
        if sentence2[len(sentence2)-1] == '.':
            return sentence1 + sentence2
        raise ValueError
    raise ValueError


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    """tests if a key is in a given dictionary"""
    return key in dictionary

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    """tests if a value is in a given dictionary"""
    allvalues = dictionary.values()
    return value in allvalues

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    """merges two dictionaries into one"""
    dictionary1.update(dictionary2)
    return dictionary1
