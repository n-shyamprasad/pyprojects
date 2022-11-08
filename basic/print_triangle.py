'''
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

rows = int(input("Number of rows: "))
def print_pattern(rows):
    for i in range(rows+1):
        for j in range(i):
            print(i, end='')
        print('')

print_pattern(rows)