'''
Write a Program to extract each digit from an integer in the reverse order.
If the given int is 7536, the output shall be "6 3 5 7", with a space separating the digits.
'''

def str_from_num(num):
    print("Orginal Number:", num)
    resultstr = ''
    while num > 0:
        digit = num % 10
        num = num // 10
        resultstr += str(digit) + ' '
        #print(digit, end=' ')
    print(resultstr)
    
str_from_num(7536)
