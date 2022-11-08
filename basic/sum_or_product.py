'''
Given two integer numbers return their product only 
if the product is equal to or lower than 1000, else return their sum.
'''
def sum_or_product(num1, num2):
    sum = num1 * num2
    if sum <= 1000:
        return sum
    else:
        return num1 + num2


result = sum_or_product(20, 30)
print("Result is ", result)

result = sum_or_product(30, 40)
print("Result is ", result)