'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    """does math on three numbers"""
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    """returns true or false"""
    return question


def main():
    """does math on some numbers and checks if answer is true or false"""
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    newanswer = choices(True)
    print(newanswer)

if __name__ == '__main__':
    main()
