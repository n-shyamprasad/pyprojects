'''
Write a function to return True 
if the first and last number of a given list is same. If numbers are different then return False.
'''
def first_last_list(numberlist):
    print("Given list: ", numberlist)

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 10]
print("result is", first_last_list(numbers_x)) 

numbers_y = [23, 34, 45, 56, 34, 5]
print("Result is ", first_last_list(numbers_y))