# example of printing text
print("Hello World")
# example of printing text a certain number of times
print("*" * 10)

# lintin the shortcut is shift+ctrl+m it lets you check for errors and shows you which line they are located in

# variables are used to store data in computer memory such as:

print("WHOLE NUMBERS")
# 1: WHOLE NUMBERS
# INTEGER
students_count = 1000
print(students_count)
# 2: FLOAT
rating = 4.99
print(rating)
# 3: BOOLEANS: can be either True or False
# they are case sensitive, and should start with a capital letter
is_published = True
print(is_published)
is_published = False
print(is_published)
# 4: STRING a text within quotes either single or double so "" or ''
course_name = "Python Programming"
print(course_name)
# can use triple quotes to format text
message = """
Salve
Blah Blah Blah
cordiali saluti, Daniel
"""
print(message)

print("ESCAPE SEQUENCES")
# used to escape characters or format
# \ (backlash) is used to escape characters that come after
course = "Python \"Programming"
print(course)
# other examples of escape sequences include:
# # which is what we are using to add comments such as this,
# \" used to add "
# \' used to add '
course = "Python \'Programming"
print(course)
# \\ used to add \
course = "Python \\Programming"
print(course)
# \n used to format to the next line whatever comes next
course = "Python \nProgramming"
print(course)

print("""
FUNCTIONS""")
# reusable pieces of code that carries out a task they are in built on different programming languages examples:
# LEN: used to get the length of a string In the example below we use it to call the course variable to return the number of characters in that string and we use brackets to return specific sections of the variable
course = "Python Programming"
print(len(course))
# we can use the square bracket to get access to a special character in the string
print(course[0])
# if we use a negative index we get the numbers from the end of the string instead
print(course[-1])
# we can also extract multiple pieces of info, in the example below we take the first three characters of the variable, as we can see though the last character of the variable 3 in this case is not included
print(course[0:3])
# if we instead remove the end variable this is the result, us getting the variables from the point we chose
print(course[0:])
# if we instead remove the starting point we get the values up to the point we chose (not counting the chosing point which in this case is 3 and would be h)
print(course[:3])
# if we don't set a starting/ending value instead we get a copy of the original string
print(course[:])

print("""
FORMATTED STRINGS""")
# used to format together strings, we call the string value of first and second using curly braces enveloping these then, we use the " " to create a space and we use + signs to formate them together
first = "Daniel"
last = "Emmingham"
full = first + " " + last
print(full)
# while this is not wrong there is another, simpler method to do this, here we start with f to call a string formatting, use curly braces to envelop the strings and we leave a space bethween them to generate the space
first = "Daniel"
last = "Emmingham"
full = f"{first} {last}"
print(full)
# we can also inbuild the len function to call in the length of a string such as like this:
first = "Daniel"
last = "Emmingham"
full = f"{len(first)} {last}"
print(full)
# here's another example, adding moltiplications
first = "Daniel"
last = "Emmingham"
full = f"{len(first)} {2 + 2}"
print(full)

print("""
FUNCTIONS / METHODS""")
# this function converts the course strings into all uppercase letters
course = "Python Programming"
print(course.upper())
# we can see that these functions do not affect the original string, to demonstrate it:
print(course)
# we could also store the value differently:
course_capital = course.upper()
# we can also use the lower method, to convert a string in all lower letters
print(course.lower())
# we also have the title method, which will capitalize the first letter of every word present in the string
course = "python programming"
print(course.title())
# another method is strip which will remove the white spaces in both the beginning and the end of the string
course = "   python programming"
print(course.strip())
# we also have lstrip and rstrip which remove either the left or the right most white spaces in the string
course = "  python programming"
print(course.lstrip())
# we also have find which is used to find a specific character or a series of characters within a string
print(course.find("py"))
# be mindful that python is a case sensitive language so if we spelled Py instead of py, we would get -1 as a result because the string was not found in the string
print(course.find("Py"))
# replace : allows us to change a character or a sequence of characters with something else
print(course.replace("p", "j"))
# in : it's a expression that produces a value used to check for the existance of a character/sequence of characters in a string, the difference bethween the find and in method is that the "find" method gives back the index of the string, while the in method gives back a boolean so true or false.
print("pro" in course)
# not in: used to see if a string does not contain a character/sequence of characters within a string
print("day" not in course)

print("""
NUMBERS = integers - floats - complex numbers""")
print("integer - x = 1")
print("float - x = 1,1")
print("complex numbers - x = 1 + 2j")  # x = a + bi

print("addition 10 + 3 =", " ", end="")
print(10 + 3)

print("subtraction 10 - 3 =", " ", end="")
print(10 - 3)

print("multiplication 10 * 3 =", " ", end="")
print(10 * 3)

print("division 10 / 3 =", " ", end="")
print(10 / 3)

print("2: division used to get integers 10 // 3 =", " ", end="")
print(10 // 3)

print("modulus which is the remainder of a division 10 % 3 =", " ", end="")
print(10 % 3)

print("2: exponent which is left (number) to the power of right (number) 10 ** 3 =", " ", end="")
print(10 ** 3)
# for all these operators we have a operator called augmented assignment operator here's some examples with the addition operator but it works the same for all of them
# x = 10
# if we want to increment x lets say by 3 we could use the following
# x = x + 3
# or we could use a augmented assigned operator:
# x += 3

print("""
FUNCTIONS THAT WORK WITH NUMBERS""")
# this returns a round number
print(round(2.9))
# absolute value of a number
print(abs(-2.9))
# python doesn't have alot of inbuilt mathematical options, to use more complex mathematical methods we have to usea a math module which is like a separate file, with python code
# for more examples check the maths.py file

print("""
COMPARISON OPERATORS""")
# used to compare values
print(" integer/float comparisons")
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 <= 20)
print(10.1 == 10.1)
print(10 == "10")
# here we get False because "10" is stored as a string type
print(10 != "10")
# != not equal operator which, returns True because 10 is a integer and "10" a string

print("""
string comparisons""")
print("bag" > "apple")
# because bag comes "after" it's considered greater
print("bag" == "BAG")
# every letter has a numerical referentiation in programming b and B have different numerical referentiations which is why the boolean outcome is False
# we can use orb to demonstrate this as follows
print(ord("b"))
print(ord("B"))

print("""
CONDITIONAL STATEMENTS""")
# we first set a condition or more
date = 31
# then we set a boolean condition after the if statement
if date > 30:
    print("end of month")
    print("new month soon")  # indentations can be as many as we want
print("""example of if condition is met
""")  # because this statement is not indented it is executed regardless of the if statement above
date = 15  # in this case because 15 is less than 30 the booleans after the if statement won't show
if date > 30:
    print("end of month")
print("""example of if condition is not met = nothing gets shown
""")
date = 15
if date > 30:
    print("end of month")
elif date >= 15:  # we can also use = to target the specific integer
    print("middle of the month")
print("""example of elif
""")
date = 1
if date > 30:
    print("end of month")
elif date >= 20:  # we can also use = to target the specific integer
    print("middle of the month")
else:
    print("start of the month")
print("""example of else
""")

print("""
TERNARY OPERATOR""")
age = 21
if age >= 18:
    print("eligible")
else:
    print("not eligible")
# nothing wrong here but we can simplify the code
age = 21
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)  # when you have a if statement where you assign a value to a statement, you can re-write this in a even simpler way

age = 18
message = "eligible" if age >= 21 else "not eligible"
print(message)  # this is a ternary operator

print("""
LOGICAL OPERATORS: and - or - not """)
# we use them to operate more complex conditions
print("""
AND operator""")
high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible")  # example of and, if both statements are true we get a return
high_income = False
good_credit = True

if high_income and good_credit:
    print("eligible")  # in this example we don't meet both conditions
else:
    print("not eligible")

print("""
OR OPERATOR""")
high_income = False
good_credit = True

if high_income or good_credit:
    print("eligible")  # in this case all we needed was either to turn True

print("""
NOT OPERATOR""")
high_income = False
good_credit = True
student = True

if not student:
    print("eligible")
else:
    print("not eligible")
# not eligible is the result due to the student statement being True
high_income = False
good_credit = True
student = False

if not student:
    print("eligible")
else:
    print("not eligible")
# while now it returns eligible due to us changing the boolean of student to False

print("""
example of more complex conditions""")
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")
# here () is used because normally the and operator would have priority over or/not
# it is not possible to have multiple () because of this fact

high_income = False
good_credit = True
educated = True
of_age = False
student = False

if high_income and good_credit or of_age and educated and not student:
    print("eligible")
else:
    print("not eligible")
# example of a even more complex use of these operators

print("""
short-circuit evaluations""")
print("example of the statement short-circuiting on the first argument")
high_income = False
good_credit = True
studend = True
# boolean operators are shortcircuits this means that when evaluating it starts from the first argument to the left
# in the case below high_income -> good_credit -> student
# however as soon as the first encountered arguments is False, the evaluation stops
if high_income and good_credit and not student:
    print("eligible")
# we changed high_income to False, and because of that the evaluation stops right there no matter what comes after.

print("""
example of or evaluation at work in this scenario""")
high_income = False
good_credit = True
studend = True

if high_income or good_credit or not student:
    print("eligible")
# here even if high_income is false it continues forward and finds good_credit which returns true, so the evaluation returns a result

print("""
CHAINING COMPARISON OPERATORS""")
# age should be bethween 18 and 65
age = 22
if age >= 18 and age < 65:
    print("comparison operator")
# in mathe we would write this rule: 18 <> age < 65
# fortunately this can be done also in python
age = 22
if 18 <= age < 65:
    print("cleaner comparison operator")

print("""
FOR LOOPS""")
# allow us to repeat a action a number of times
# we could rewrite code a number of times OR we could use loops to create repetitions

for number in range(3):
    print("attempt", number)
# number printed behind attempt allows us to show the attempt numbers in this scenarios
# it shows 0 - 1 - 2 it starts from 0 because of how memory addresses are calculated in computers
# to make it user friendly we can add after number a +1 to show 1-2-3 like this:
for number in range(3):
    print("attempt", number + 1)
# we can take it one step further and make dots show like this:
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")
# * multiplies the dot (.) at every new attempt

# we also know that the number 3 isn't included and we can see that in the first test 0 - 1 - 2
# to fix this we can:
for number in range(1, 4):
    print("attempt", number, number * ".")
# this makes us start at 1 and finish before 4
# this way we don't need to add 1 to number every time

print("""
examples of steps""")
# we can also pass a third argument as a step
# FIRST ARGUMENT = starting point
# SECOND ARGUMENT = number of attempts
# THIRD ARGUMENT = steps
for number in range(0, 20, 3):
    print("attempt", number, number * ".")
# 0 = starting point - 20 = number of attempts - 3 = steps = 0-3-6-9-12-15-18
for number in range(1, 12, 4):
    print("attempt", number, number * ".")
# 1 = starting point - 12 = number of attempts - 4 = steps = 1-5-9

print("""
FOR ELSE""")
print("example of break use")
successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break  # used to break the loop if/when the if statement returns true
# the indentation is important the first 2 lines after the for loop belong to the for loop
# while thw two following the if loop belong to the if loop

print("""
FOR ELSE example""")
# what if the statement goes through and isn't successful and we want to deliver a different message?
# what if, as for example, we attempt three times, and it doesn't go through and we want to send a message saying that it didn't work?
successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:  # if we never break out of the loop above then the else statement will be executed
    print("attempted 3 times and failed")
# if we changed successful = True to False the else statement would not be executed instead

print("""
NESTED LOOPS""")
for x in range(3):  # called outerloop
    for y in range(3):  # inner loop
        print(f"({x}, {y})")
# f (formatted strings) we are gonna use them to show coordinates
# the inner loop is a child of the outerloop
#  the print f is the child of the inner loop
# after one full round of the inner loop, so in this case:
# x, 0 - x, 1 - x, 2
# we move back to the outerloop and repeat the process so:
# x+1, 0 - x+1, 1 - x+1, 2 and so on

print("nested loop starting from 0")
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})")


print("""
ITERABLES""")
# with the following function we can get the type of an object
print(type(True))  # object of type bool
print(type(5))  # object of type int(integer)
print(type(range(5)))  # object of type range
# in python we have primitive types such as booleans numbers, strings
# and complex types such as range
# range is iterable which means you can iterate over it or use it on a for loop
# for x in (range(5)) is an example that x can be iterated

# strings are also iterable:
for x in "python":
    print(x)
# in each iteration we'll get one character of the word python in this case

# we have another complex type called list
for x in [1, 2, 3, 4]:
    print(x)
# this turns one iterable object from that list

print("""
WHILE LOOPS""")
# used to repeat something as long as the condition is True
number = 100
while number > 0:
    print(number)
    number //= 2  # shortened version of number = number // 2
    # we start with the number value, and divite it by a certain amount and repeating such task long as long as the while statement is true

print("""
run the following in the terminal""")
# command = ""
# while command.lower() != "quit":
# command = input(">")
# print("ECHO", command)  # echoes our result
# .lower allows us to check for quit with all variations of lower/upper case letters
# command = input(">") stores the new data for us in command
# the in-built terminal is read only which won't work for this command
# run this in the normal terminal wirting:  python3 filename.py (name of the file)


print("""
INFINITE LOOPS""")
# while True:  # having a infinite loop means we don't need to ine command and setting it to a empty string
#    command = input(">")
#    print("ECHO", command)
#    if command.lower() == "quit":
#        break
# because the command runs forever for aslong as it's True we need to add a if statement (in this case with quit) with a break so that IF we type that word we break out of the loop

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
# greet is the name of the function
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

print("""
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