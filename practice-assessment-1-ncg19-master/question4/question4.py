'''
question4.py

Fix the errors so that this code runs when called
from the commandline.
'''

def reverse_words(input_string):
    '''Reverse the order of the words between spaces'''
    # create a list of each word
    words = input_string.split()
    # reverse the list
    words = words[::-1]
    # put back together in a string
    rev = ''
    for i in words
        rev += i + ' '
    # return the string
    return rev




def main():
    '''Main function to be run first.'''

    my_string = 'Imperial College London'

    # count number of words in string
    reverse_string = reverse_words(my_String)

    # print how many words were counted
    print 'The original string is: {}'.format(my_string)
    print('and the words reversed is: {}'.format(reverse_string))

if __name__ == '__main__':
    main()
