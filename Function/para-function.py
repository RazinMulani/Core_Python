# Parameterized function: A parameterized function is a function take parameter(inputs)a perform a task.
# Paramteres is variable written inside the paranthesis of a function definition.

# you write one code so many different different types
# 1)
def add(a,b):
    c = a+b
    print(c)
add(10,20)

# 2)
def add(a,b):
    print(a+b)
add(45,10)

# 3) get value from user

def add(a,b):
    print(a+b)
x = int(input("Enter The value of x:"))
y = int(input("Enter The value of y:"))
add(x,y)

