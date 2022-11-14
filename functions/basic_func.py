'''
Functions
'''

#create a function that takes two arguments, name and age, and print their value.
def func1(name,age):
    print(f"name: {name}  age: {age}")

print("--------Test1--------")
func1("JHon",30)


#function with variable length of arguments
def func2(*args):
    idx = 0
    for i in args:
        idx = idx + 1
        print(f"param{idx} - value: {i}")

print("--------Test2--------")
func2("JHon",30)
func2(10,20,30)


#Return multiple values from a function
def calculate(a,b):
    return (a+b),(a*b)

print("--------Test3--------")
a,b = calculate(10,20)
print(f"a: {a}, b:{b}")


#nested functions
def outer_fun(a,b):
    square = a ** 2
    def addition(a,b):
        return a+b
    
    add = addition(a,b)
    return add + 5

result = outer_fun(5,10)
print("--------Test4--------")
print(f"result: {result}")


#recursive function
def addition(num):
    if num>0:
        return num + addition(num - 1)
    else:
        return 0
res = addition(10)
print("--------Test5--------")
print(f"Recursive Addition: {res}")


#assing function to varible
new_fun = func1
print("--------Test6--------")
new_fun("this function created from func1", 100)

#Generate a Python list of all the even numbers between 4 to 30
print("--------Test7--------")
print(list(range(4,30,2)))


#Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print("--------Test8--------")
print(f"Given list: {x}")
print(f"Max number: {sorted(x,reverse=True)[0]}")
print(f"Max number: {max(x)}")
