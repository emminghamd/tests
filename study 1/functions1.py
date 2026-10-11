print("""
DEFINING FUNCTIONS - ARGUMENTS""")

# a function is a reusable piece of code for example: print() - round()
# we use a function to break large code into smaller, more maintainable/reusable chunks(functions)


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome")


greet("Daniel", "Emmingham")
greet("Davide", "Abbrescia")
# def (define) allows us to create(or define) our own function
# first_name, last_name are our parameters
# gree is the name of the function
# we call the function greet in this case since we use it to greet people
# once we are done with the indentations (the prints) we need to call it
# greet ("Daniel", "Emmingham") does exactly that
# and because on the function we set two parameters (first_name, last_name)
# here we are setting them as "ARGUMENTS"
# difference bethween parametere and argument:
# parameter: input that you define for your function
# argument: actual value for the given parameter
# all the parameters defined by a function are required
# so if in a function we set up two parameters and we remove one argument we get a typeerror

("""
TYPES OF FUNCTIONS""")


# def greet(name):
#    print(f"Hi {name}")
# in programming we have two types of functions:
# 1: functions that perform a task such as the one above
# 2: functions that calculate and return a value such as the one below:
# round(1.9)

# we can also rewrite the greet function (the first), but in the second form:
def greet(name):
    # this way of writing it doesn't allow us to reuse the function later on
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi [name]"  # we set return to return the value effectivly
# making this a function that returns a value rather than perform a task


message = get_greeting("Daniel")
# now we store the value in a separate variable which here we call message
# this second form isn't tied to printing something in the terminal
# which makes it reusable
# we could print it in the terminal
print(message)
# or we could use the following to write a message to a file for example:
file = open("content.txt", "w")
file.write(message)

print("""
all functions return None by default """)


def greet(name):
    print(f"Hi {name}")


print(greet("David"))
# we can also sent this in the print function
# we get back None, which is the greet value of this function
# in python all functions return by default the None value
# none is an object that represents the absence of a value
# even though it's a function that returns a value, it's still considered a function that carries out a task

print("""
we can change that by attributing them a value """)


def greet(name):
    return "..."
# now because we gave a value that isn't the default (None) we get back said value


print(greet("David"))

print("""
KEYWORD ARGUMENTS""")


def increment(number, by):  # return increment by given value
    return number + by


# this returns a value so we can store in a variable like result
result = increment(2, 1)
print(result)

print("""
the code can be simplified as such:""")


def increment(number, by):
    return number + by


# first it will get the result and store it as a variable (that we don't see)
print(increment(2, by=1))  # by=1 is a keyword argument
# then it will pass that variable as an argument in the function

print("""
DEFAULT ARGUMENTS""")


def increment(number, by=1):  # we can make the by parameter optional
    return number + by


print(increment(2))

# we can also pass a second argument in increment in which case


def increment(number, by=1):
    return number + by


print(increment(2, 5))
# we can make the by parameter optional by ading a parameter in increment
# just be aware though that any optional parameter need to be placed after the required parameter
# for example: (number, another, by=1) - another being the optional parameter that we'd want to add
# this will result in the by=1 parameter being optional

print("""
XARGS""")
# there are times that we want a function that takes a varied number of arguments


def multiply(x, y):
    return x * y


multiply(2, 3)
# but what if we wanna pass multiple arguments here such as: multiply(2, 3, 4, 5)

# to do it we replace the parameters with a parameter that is the collection of parameters
# example: *numbers


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)
# use [] to create lists and () to create topols
# a topol is similar to a list, as it's a collection of objects
# the difference though is that we cannot modify this collection
# topols are iterable

("""
example of iterable topols""")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number  # can also write total = total * number
    return total  # returns the total, make sure it's indented properly


# now we can print the multiply to get the total of all these values
print(multiply(2, 3, 4, 5))
