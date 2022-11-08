'''
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
'''
def remove_chars(word, n):
    print('Original word: ', word)
    result = word[n:]
    return result

print("Result")
print(remove_chars('pynative', 4))
print(remove_chars('pynative', 2))