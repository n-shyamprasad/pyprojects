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