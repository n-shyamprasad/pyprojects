'''
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''
def num_div_five(mylist):
    print("Input list: ", mylist)
    print("Divisible by 5: ")
    for num in mylist:
        if num % 5 == 0:
            print(num)


mylist1 = [10, 11, 15, 20, 21, 25]
print(num_div_five(mylist1))