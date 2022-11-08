'''
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display p, n, t, v.
'''
i_word = input("Enter word :")
size = len(i_word)

def print_even_char(i_word):
    print("Printing even charcheters from input word")
    for i in range(0, size - 1, 2):
        print("index[", i, "] ", i_word[i])

print_even_char(i_word)

def print_even_char1(i_word):
    print("Print even chars from word")
    lst = list(i_word)
    for i in lst[0::2]:
        print(i)

print_even_char1(i_word)

def print_even_char2(i_word):
    print("print even chars from word")
    for i in i_word[0::2]:
        print(i)

print_even_char2(i_word)