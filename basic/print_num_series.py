'''
Write a program to iterate the 
first 10 numbers and in each iteration, print the sum of the current and previous number.
'''
def print_num_series():
    prev_num = 0
    for i in range(1,11):
        sum = i + prev_num
        print("Current number ", i, "previous number ", prev_num, "sum is ", sum)
        prev_num = i

print_num_series()