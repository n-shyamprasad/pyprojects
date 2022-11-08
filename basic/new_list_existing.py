'''
Given a two list of numbers, write a program to create a new list 
such that the new list should contain odd numbers from the first list and even numbers from the second list.

Input:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected:
result list: [25, 35, 40, 60, 90]
'''

def new_list_from_two_list(list1, list2):
    merged_list = []

    for num in list1:
        if num %2 != 0:
            merged_list.append(num)

    for num in list2:
        if num % 2 == 0:
            merged_list.append(num)
    
    return merged_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(new_list_from_two_list(list1, list2))
