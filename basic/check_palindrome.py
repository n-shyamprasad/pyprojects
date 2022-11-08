'''
Write a program to check if the given number is a palindrome number.
'''
def palindrome(num):
    print("Orgnial NUmber: ", num)
    org_num = num
    rev_num = 0
    while num > 0:
        rem = num % 10
        rev_num = (rev_num * 10) + rem
        num = num // 10
    if org_num == rev_num:
        return "is palindrome"
    else:
        return "is not palindrome"


print(palindrome(242))
print(palindrome(112))