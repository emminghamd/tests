# print displays whatever message is in it and returns it
import random  # importing the module needed
import math
print("Functions types")
# python has in built functions like print/input/len
# also third-party like panda/pyspark
# user defined functions made by users (us)

print("SPECIAL CHARACTERS\\\'\"")
# used in torder to return these characters in the text
# \"" returns "
# \' returns '
# \\ returns \
print("example of useful use", "path: C:\\Users\\Uni\\Documents")
# \n returns to the next line
print("returns to the \n next line")
# \t adds orizzontal tab
print("add orizzontal\ttab")
# \b adds backspace
print("add\b backspace")
# use 1 print to make 3 separate messages on three separate lines:
# \ before every line: \ sign and orizzontal tab - the last s of exercises removed
# we can use in this case triple quotes instead of \n,
# adding both would created a space bethween every new line since they both create a line
print("""\t \\ Special 
         \t \\ characters 
         \t \\ exercises\b """)

# it's a in-built function
# used to display messages in output for users
# can be used to communicate, show results, debugg, test
print("PRINT")

print("Variables")
# variables are like a box and we can give it:
# a number, a integer, a string, a calculation
# this box can be reused in your code
# can be changed
# to set up a variable we first set up a variable then we give it a value.
# examples: x = 1.5 - names = 2
# then once we want to execute it we will not use the value BUT the variable name for example:
# print(x) - print(names)
# once print is used the machine will look into the box and determine
# what the last value of the given variable is and return it
# for example if we were to now say:
# x = 1 y = x + 3 and we printed both before the y variable was set and after
# weìd have different results
x = 2
print(x)
y = x + 3
print(y)

print("example of variable concatenations")
price_shirt = 25.00
price_jeans = 45.50

qty_shirt = 3
qty_jeans = 1

total_shirt = price_shirt + qty_shirt
total_jeans = price_jeans + qty_jeans

subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)
discount = subtotal * 0.10
print("Discount:", discount)
total_discounted = subtotal - discount
print("Total discounted:", total_discounted)


print("another example of variables")
# name is our variable, Dani it's current value
name = "Dani"
# here it understands that name is a variable so it doesn't execute it
# but rather finds it's value to execute
# while it understands that the text bethween "" is the static part
# the space bethween the variable and the text is given by the comma bethween the two
print(name, "considers Python")
print(name, "likes Python")
print("Therefore", name, "is studying Python")

# what if we want to swap the name Dani with another? all we need to do is
# change the stored variable value with another of our chosing.
# for example we could:
name = "Rob"
# to change it but of course, because python executes code line-by line
# python wouldn't know that we changed the variable's value now unless
# we execute it again afterwards like this:
print(name, "considers Python")
print(name, "likes Python")
print("Therefore", name, "is studying Python")

# furthermore, if we feel like we use a value alot and would like it to be static
# we can allways convert it into a variable and change it:
language = "SQL"
print(name, "considers", language)
print(name, "likes", language)
print("Therefore", name, "is studying", language)
# -----------------------------------------------------------------------
# VARIABLE RECAP
# used to make programs dynamic - named to store a value
# stored in memory - reusable anytime
# ----------------------------------------------------------------------
print("INPUT FUNCTION\n")
# used in websites to let people type passowrds, names and the likes
# in ai/browsers it's the search bar for example
# it's used to get "something" (input) from the user
# when we are writing code and we'd like to get something from the user
# we write input("enter value") python first runs it and displays it in the output
# at this point the application waits for a input from the user
# once value is given from the user, said value is returned back to our code
# ----------------------------------------------------------------------
# name = input("Enter Your Name:")
# after this message our code is simply waiting for a input
# if we were to stop here, once the input is given it's also lost
# so lets do something with it:
# country = "Italy"
# print("you are", name) # now we actually use the user's variable
# -----------------------------------------------------------------------
# "Italy" is a example of a hard coded values
# one that we can change in the code but the user can't since it's hard coded in the code
# "name" is a example of a dynamic values, since it's whatever value the user gives it
# -----------------------------------------------------------------------
# in this example below  we mix the two name gives back the user input while country a hard coded value
# name = input("Enter Your Name:")
# country = "Italy"
# print(name, "comes from", country)
# ----------------------------------------------------------------------
# in conclusion: input makes your program interactive
# it lets your program ask questions and interact with the user
# ------------------------------------------------------------------------
# example of what we learned so far:
# x = "A" # hard coded variable and it's value
# print(x) # ask the pc to fetch the variable's value and return it
# y = input("Enter Value") # use input to ask the user for a dynamic value to give to a variable
# print(y) # print the user's variable's value
# ----------------------------------------------------------------------------------


print("DATA TYPES\n")
# python automatically detects and stores data by type, types such as:
# integer (whole number) / a = 10 (for example)
# float (decimals) a = 1.2 (decimals)
# comples numbers 3 + 5j
# str (string) = any type of text = print("hello") / hello is the str
# bool (boolean) = True or False (upper case sensitive) used to make decisions
# data & time = date, time, datetime
# date = 1-09-2026 / time = 22:25:30 / datetime = 1-09-2026 22:25:30
# python is also smart enough to understand which data type can do what:
# for example:
# print("Hello").upper() would put all letters of the string in uppercase
# but when applied to a integer for example:
# a = 50 print("a").upper() we would return a error
# because python detects a as a integer and integers can't use .upper()
# another example: 2 + 3 = 5 but what happens if we have "2" + "3"?
# what happens is that python returns 23
# that's because it treated "2" + "3" as a concatenation of strings

# data types have three different values:
# 1) no value = none
# 2) single value (primitive data types) = integers, floats, str, booleans
# because they only hold one value
# 3) multi values (advanced data types) = called also data structures, collections, containers
# lists = list[1, 2, 3]
# dictionaries = dict{"a":1, "b":2, "c":3}
# set{1,2}
# tuple("a","b","c")
# array("i", (10, 20))

a = 10  # int
b = 3.15  # float
c = "hello"  # str
c = "1234"  # str
d = True  # bool (case sensitive)
e = False  # bool (case sensitive)
f = None  # special value used to show the absence of data
g = ""  # str - blank-  not to be confused with the None value
h = " "  # str - empty space not to be confused with the value None
# -----------------------------------------------------------------------
print("DATA TYPES, FUNCTIONS, METHODS\n")
# in order to utilize data (values) we use functions
# which in return gives us a new value
# three main types of functions:
# 1) standalone functions = print() - type() - lan()
# 2) methods of class = upper() - replace()
# 3) operations = +, *, /, <, >, ==, in, or,
# all these functions come from the standard python library
# we also have third party libraries like:
# Pandas - numpy - tensorflow -
# user defined functions which are something we code and create on our own
# in the standard library we have in built modules:
# we have the standalone functions here = print() - type() - lan()
# class str and we have methods that are attached only to those classes:
# for example upper() replace()
# for the class integer we have: to byte()
# we also have the math module but this one isn't in built and has to be imported:
# import math - is how we'd import it
# some functions might work with certain class types some will not
# for example a string class can work with upper() and len() but it will return error with math modules.

# your data (values) are objects that are connected to a specific data class
# and each class has multiple possible methods, it can use any methods within it's class
# and it may be able to use other methods from other classes
# they are however completely forbidden from using another datatype class


# functions = independent block of code
# methods = functions belong to objects/classes
# example of function syntax:
# function_name(value) = print("hello") = print is the function, hello the value
# syntax for methods:
# value.method_name() = here we start with the value and then the method name
# example of method syntax:
# "hello".upper() / 50.bit-length() = hello is the value, upper the method
# ------------------------------------------------------------------------
print("example of type functions\n")
text = "hi"
number = 10
truth = True

print(type(text))  # returns the data type of a value
print(type(number))  # so that we know what kind of object it is
print(type(truth))
# ----------------------------------------------------------------------
print("example of len functions\n")
text = "hello"
# number = 10

print(len(text))
# print(len(number)) - if we were to run this print we'd get a typeerror because len doesn't work for integers
# ------------------------------------------------------------------------
text = "hello"
# number = 10

print(text.upper())  # upper() converts all letters in a string to uppercase
# print(number.upper()) - this will return typerror due to a integer
# -----------------------------------------------------------------------
number = 10

# returns the number of binaries in this case the binaries for 10 is 4
print(number.bit_length())
# ------------------------------------------------------------------------
print("DATA TYPES challenge:")
# type and print your age, height, name, if you are a student, a empty value
# print also their type and length
age = 36
height = 178.5
name = "Dani"
student = True
needs_value = None

print(age)
print(height)
print("name")
print(student)
print(needs_value)

print(type(age))
print(type(height))
print(type("name"))
print(type(student))
print(type(needs_value))

# print(len(age)) - can't use the len function on a int
# print(len(height)) - can't use the len function on a float
print(len("name"))
# print(len(student)) - can't use the len function on a bool
# print(len(needs_value)) - can't use the len function on a None
# ------------------------------------------------------------------------
print("\nWORKING WITH STRINGS")
# strings are just text bethween quotes/double quotes
# why should we care about strings? because it's everywhere:
# filenames, user input, web data, logs
# it is one of the most likely types of values to be messy, with typos etc
# but at the same time it's one of the most used and often holds alot of valuable information
# --------------------------------------------------------------------
print("string functions: categories")
# CLEANING: clean whitespaces: lstrip() - rstrip() - strip() - clean cases: lower() - upper()
# SEARCH: startswitch() - endswith() - find() - "a" in "cat"
# VALIDATION: isalpha() - isnumeric()

print("\nTYPE: type - str")  # TYPES: type() - str()
name = "Dani"
age = 30
print(type(name))
print(type(age))
# print("Your age:" + age) - type error because we only merge same types of data
# we can use str to convert any value into string value
print("Your age:" + str(age))  # str converts the age int value into a str
# making the merging of the two possible
# because str stay within that line, it doesn't permanently change age into a str which allows us to:
age = age + 5
print(age)  # we can still work on the int
age = str(age)  # we can once again convert it into a str if we want but!!!
print(type(age))
# age = age + 5 if we execute it now we'd get a error because it's now a str and not a number
# -----------------------------------------------------------------------

print("\nMATH")
print("\nLEN - COUNT")   # MATH: len() - count()
password = "123a541si"
# returns the number of items/characters in a value (in this case a str)
print(len(password))

if len(password) < 8:  # this is how we'd setup to to allow for a minimum number of characters that the user has to return
    print("Your password is too short!")
# ---------------------------------------------------------------------
text = """
Python is easy to learn.
Python is powerful!.
Many people love python. 
"""  # because the last python isn't uppercase the print result won't consider it
print(text.count("Python"))  # Python will return 2 python will return 1
# use case: count how many unwanted characters are present in my data
# for example if we didn't want there to be a ! in our code we could set:
# count("!") to figure out exactly how many(1) and where they are located
# ----------------------------------------------------------------------
print("\nTRANSFORMATIONS")
# TRANSFORMATIONS: replace() - "R" + "i" - f() - split() - "ha" * 2 - extraction: "cat" [0] - "cat" [1:3]

print("\nREPLACE")  # replace() allows us to replace a value with another
price = "1234,56"  # in this example we need to replace the comma with a dot
print(price.replace(",", "."))  # we used replace to replace the , with a .

phone = "176-1243-43"  # replace - with /, nothing or with a space
print(phone.replace("-", "/"),
      phone.replace("-", ""),
      phone.replace("-", " "))

price = "$1,299.99"  # multiple changes simultaneously
print(price.replace("$", "").replace(",", ""))  # removed $ and ,
# ------------------------------------------------------------------------
print("\nreplace exercise")
phone = "+49 (176) 123-4567"  # return 00491761234567
print(phone.replace("+", "00").replace(" ",
      "").replace("(", "").replace(")", "").replace("-", ""))
# ----------------------------------------------------------------------

print("\n+ OPERATOR")  # concatenate two or more strings using the + operator
first_name = "Bob"
last_name = "Ross"
# " " to add a space bethween the two variables
full_name = first_name + " " + last_name
print(full_name)

# USE CASE: build dynamic file paths
folder = "C:/Users/Uni/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)
# -----------------------------------------------------------------------
print("\nf-string")  # way to build and format strings
# lets you put variables and expressions directly inside the string value
name = "Rob"
age = 30
is_student = False
# print("My name is " + name + ", I am " + str(age) + " years old, my student status is " + str(is_student) +".")
# because age and is_student aren't str we need to use str() to change them to str
# this is hard to read tere are alot of + signs, types and spaces

# this is the modern way to do it
# print(f"{}"")
print(
    f"My name is {name}, I am {age} years old, my student status is {is_student}.")
# automatically lets python handle non-string values and converts them
# way more readable and managable

# not only variables, we can also use it for expressions
# the converted str value within {} returns our variable result in the form of a str
print(f"2 + 3 = {2 + 3}")

# if we wanted to print the brackets {} as part of the text we have to escape them:
print(f"{{This is me}}")  # all we need to do is use them twice
# -----------------------------------------------------------------------
print("\nsplit()")
# often we have many different types of values: Adam - 24 - USA
# in that example we have a name (string), age (integer), and nation (string)
# we use split() to divide them so that we can use them better
# aswell as converting them all into strings
# we'd start by saying split("-") to remove the - (dash)
# what follows is us getting a list of items without said dash
# ["Adam", "24", "USA"]

stamp = "2026-09-20 14:30"  # lets separate the date and the time
print(stamp.split(" "))  # by adding a space we separated the two values

stamp = "2026-09-20"  # here we remove the - and get the three values
print(stamp.split("-"))

csv_file = "1234,Max,USA,1970-10-05,M"  # other example
print(csv_file.split(","))
# ----------------------------------------------------------------------
print("\nString Repetition")  # can use it to repeat a string multiple times
print("ha" * 3)
# can use to create clear sections in output, for example a division line bethween paragraphs
print("-" * 70)
# ----------------------------------------------------------------------
print("\n EXTRACTION")  # used to extract specific parts of our strings
# lets take the string ("hello")
# positive index (left to right) = h = 0 e = 1 etc
# negative index (right to left) = 0 = -1 i = -2 i = -3 e = -4 h = -5
# lets say we want to extract a specific character of said string
# [0] would extract the h starting from the positive index
# [-5] the h starting from the negative index
# what if we want to extract the first two values?
# [start:end] BUT because it won't include the ending value we'd have to have end be i
# the result would be he
# if we decide to do it from the negative index: [-5:-3] = he
# so remember the starting position is 0 by default and the end is NOT included
# if we want to skip certain characters for example we want to skip the h
# [1:0] this would skip the h and return ello
# [start:end:step] allows us to skip a position for example:
# [0:4:2] 0 = starting position 4 = end position 2 = number of steps
# this will result in hl: h is 0 e is step l is included l is step o is excluded since we skip the end is NOT included by default

text = "Python"  # indexes & slicing
print(text[0])  # extracting first character from the positive index
print(text[-6])  # extracting first character from the negative index
print(text[5])  # extracting character from the positive index
print(text[-1])  # extracting last character from the negative index
print(text[3])  # extracting h from the positive index
print(text[-3])  # extracting h from the negative index

date = "2026-09-20"  # slicing
print(date[0:4])  # extracting the year from the positive index
print(date[-10:-6])  # extracting the year from the negative index
print(date[:4])  # if we leave the starting point empty python defaults it to 0
print(date[5:7])  # extracting the month from the positive index
print(date[-5:-3])  # extracting the month from the negative index
print(date[8:])  # extracting the day from the positive index
print(date[-2:])  # extracting the day from the negative index

# when do we use positive/negative indexes?
# start from whichever side we are closest
# in the example given above we'd start with the positive if we wanted the year and negative fi we wanted the day
# ----------------------------------------------------------------------
print("\nCLEANSING DATA: REMOVE SPACES")
# what if we have spaces in the string we want to remove?
# lstrip() for spaces one the left rstrip() for spaces on the right
# with strip() instead we can remove both side's spaces simultaneously
text = "   Hello   "
print(text)  # unvaried result
print(text.lstrip())  # left space removed
print(text.rstrip())  # right space removed
print(text.strip())  # removes spaces from both ends
text = "   Hi there  ".strip()  # we can also attach it to the variable
print(text)
# the best practice since you never know where users might add spaces is to use .strip() to remove spaces from both ends

# the strip method can't remove white spaces inside your text
text = "###ABC###".strip("#")  # we can also remove values
print(text)

# use case: to detect extra spaces we can check the length before and after strip() to find unwanted spaces
text = "  Engineering"
print(len(text))  # this tells us the length of our variable 13
print(len(text.strip()))  # like this we can tell it to apply the strip method
print(len(text) - len(text.strip()))  # to calculate the amount of white spaces
# tells us that the variable isn't equal telling us there's, in this case the 2 spaces
print(len(text) == len(text.strip()))

nr_of_spaces = (len(text) - len(text.strip()))
is_clean = (len(text) == len(text.strip()))
print("Nr of spaces:", nr_of_spaces)  # tells us how many white spaces
# false because text is 13 / text.strip 11
print("My data is clean?", is_clean)
# -----------------------------------------------------------------------
print("\bCLEANING DATA: case conversion")

# use case: standardize text to our wanted values
# in the example below lets say a user inputted wrong upper/lower cases
# how do we fix that?
text = "python PROGRAMMING"
print(text.lower())  # changes every letter to lower case
print(text.upper())  # changes every letter to lower case
# use case: we use it to clean up data before searching
# to prevent case-based mismatches during search or comparisons

search = "Email ".lower().strip()
data = " emAil".lower().strip()
print(search == data)  # would turn false if we didn't add the .lower).strip()
# ----------------------------------------------------------------------
print("\nCHALLENGE")
# convert: "968-Dani, ( Electricti@n );; 36y  "
# into: name: Dani | role: electrician | age:36

info = "968-Dani, ( Electricti@n );; 36y  "
print(info.lower().strip().replace("968-", "name: ")
      .replace(",", " | ")
      .replace("(", "role: ")
      .replace("@", "a")
      .replace(");;", " | age:")
      .replace("y", "")
      )
# -------------------------------------------------------------------------
print("\nSEARCH")
# to check and compare specific parts of a str with something we want
# if there's a match the return is the boolean True.
# startswith("") positive index endswith("") negative index or "in" operator
# with find() we can search the starting position of our value (even if the value is multiple inputs)

phone = "+33-284-3245"
# checks if the string starts with a specific value
print(phone.startswith("+39"))
# for the italian country code +39 and returns the boolean (False in this case)

file = "data_backup.csv"
print(file.endswith("csv"))  # example with finding files extensions

email = ("notamail@hotmail.it")
# checks if the string ends with a specific value and returns the boolean
print(email.endswith("it"))
print("@" in email)  # in operator checks for a specific word in a string
# as for the example this is a way to find if the user inputted a invalid email or other type of input

url = "https://api.company.com/v1/data"  # check if the url is an api endpoint?
print("api" in url)
# -----------------------------------------------------------------------
# is great when combined with other methods to add dynamics
print("\nFIND = find()")
phone1 = "+39-284-3245"
phone2 = "39-731-9637"
print(phone1[4:])  # getting the phone number without country code
print(phone2[3:])  # because we don't have a plus we have to start from 3
# but this doesn't work when the country code length changes so:
phone3 = "0033-385-8473"  # lets use the find method to start from the first -
print(phone3.find("-"))  # n4 is the outcome of the word before the one we want
print(phone3[phone3.find("-"):])  # to fix the fact that we see the - we:
print(phone3[phone3.find("-")+1:])  # add +1 to start from the next word
# ----------------------------------------------------------------------
print("\nVALIDATION")
# validating out code, for example if the user is supposed to input only letters for the input of their country we validate that
# example:
country = "Netherlands"
# isalpha() str method returns boolean that checks if the string has only letters
print(country.isalpha())

country = "Italy1"
print(country.isalpha())  # returns false due to the typo 1 at the end
country = "Italy!"
print(country.isalpha())  # returns false due to the typo ! at the end
# we are validating only letters with isalpha()
# ---------------------------------------------------------------------
phone = "39464547892"
# isnumeric() str method, returns boolean, checks if the str has only numbers
print(phone.isnumeric())
phone = "39-464547892"
# same scenario here if we have anything that isn't a number the boolean turns False
print(phone.isnumeric())
phone = "4.05"
# this is also true for special characters even if the special character would make the number look like a float
print(phone.isnumeric())
# -----------------------------------------------------------------------
# numbers belong to the data type value of single values
print("\nWORKING WITH NUMBERS")
# for complex math and functions we also have the math module: import math
# -----------------------------------------------------------------------
print("\nTYPES:")  # numeric types: type() - int - float - complex data
x = 5  # integer
y = 5.7  # float
# complex = built-in function creates a complex number using real and imaginary parts = 2 + 3j
# used to represent for example: percentages, averages, temperatures
z = 2 + 3j  # complex data
print(type(x))
print(type(y))
print(type(z))

x = "24"  # how to convert this str to a number?
print(type(x))  # tells us that it's a float and not a number
print(x * 3)  # here instead of multipling it repeats the string

x = int(x)  # int() is a in-built function that outputs a int value (if compatible)
print(type(x))  # now it recognizes x as a int
print(x * 3)  # and properly multiplies it
x = 3.14  # what happens if we try to convert a float into a int?
print(int(x))  # it becomes 3 losing it's decimal numbers

x = 3  # what if we want to convert a int into a float?
print(float(x))  # built-in function returns a float if compatible
x = "3.14"  # can also convert a str into a float
print(float(x))  # if compatible

x = 3  # real
y = 4  # imaginary
# converts to a complex number using a real and imaginary part
print(complex(x, y))
# ----------------------------------------------------------------------
print("\nMATH OPERATORS")  # math operators: + - * / // % **
print(2 + 3)  # addition
print(5 - 3)  # subtraction
print(4 * 3)  # multiplication
print(7 / 2)  # division
print(7 // 2)  # floor division: divides two numbers and rounds down to a int
print(7 % 2)  # remainder: leftover part after dividing returns 0 or 1 used to check if a number (7 in this case) is even(the case of 7) or odd
print(2 ** 3)  # exponentiation: raises a number to the power of another number, the first number is the base, the second the exponent in the example: 2*2*2
# ----------------------------------------------------------------------
x = 2
x += 3  # shortcut of x = x + 3
print(x)
x -= 1  # shortcut of x = x -1
print(x)
x *= 2  # shortcut of x = x * 2
print(x)
# ----------------------------------------------------------------------
print("\nROUNDING")  # rounding: abs() round() ceil() floor() trunc()
# to measure distances we can use abs()
# built-in function - returns int = returns the absolute(non-negative) value of a number
# absolute number outcome useful for measuring distance/size regardless of direction
print(abs(2-10))

# Rounding Numbers:  useful when numbers are messy, we round them to make them easier to read
# use case: lets say we have the decimal numbers bethween 1 and 2
# we call those closer to 2 the ceiling and those closer to 1 the floor
# for readability we can try to round the number up to the closer of the two
# math.floor(x) rounds to the floor math.ceil(X) to the ceiling
# we also have round(x) which rounds to the nearest number up or down depending on what's closer
# we also have bankers rounding ties (like .5) go to the nearest even number
# this isn't about the distance it's about wether a number is odd or even
# example of bankers rounding: 1.5 = 2 - 2.5 = 2 - 3.5 = 4
price = 35.54346545
print(round(price))  # since we are in bethween numbers it rounds to the even
# round(number.digits) rounds the number to the specific number of decimal places
print(round(price, 1))
print(round(price, 3))  # shows 3 digital numbers 35.543
# not a in-built function need to call the module "import math" before using this and other complex math modules
print(math.floor(price))
# we get back the floor aka bringing the price down to the closest integer
print(math.ceil(price))  # returns ceiling
# -----------------------------------------------------------------------
# mathtrunc(x) cuts off the decimal and keeps the whole number (no rounding)
print(math.trunc(price))  # cuts off the decimals leaving us with a int
print(int(price))  # this is a in-built way to get rid of the decimals
# if you have already imported math, method use trunc, it makes your intent clearer
# if we haven't used math and don't intend to, we might aswell use int

# use cases:
# round: we use the round to make numbers easier to read, code easier to read
# ceil(): data engineering - splitting data into pages or batches, patching, resource allocation, to make sure we allways have enough resources and that we are not missing anything
# -----------------------------------------------------------------------
print("\nADVANCED MATH:")  # advanced math: sqrt() sin() cos() log()
# -----------------------------------------------------------------------
print("RANDOM:")  # random: random() randint()
# random function - returns float - returns a random float bethween 0.0 and 1.0
print("random:", random.random())
# what if we want to roll a random integer (for example rolling a dice or selecting a random name from a list)
# generates a random number bethween two given numbers
print("randint:", random.randint(1, 10))
# case scenarios: generate test data for like: age, id, prices
# random sampling: pick a smaller random part of a huge dataset
# -----------------------------------------------------------------------
print("\nVALIDATION:")  # is_integer() isinstance()
x = 7.0  # we'd like to check if this is a integer
print(x.is_integer())  # returns True because 7.0 doesn't have decimal points
y = 7.1  # now it returns False because there's a decimal
print(y.is_integer())
# -----------------------------------------------------------------------
# sometimes we might get numbers like: 40.00 or the likes and we'd like to check if they are real numbers,
# and if so we can use is_integer to test first whether changing them into integers would make us lose any data
# isinstance(value, type) can be used to check if a value belongs to a certain type or not
x = 70
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, bool))
# -----------------------------------------------------------------------
# generate a random integer between 1 and 100
# check if the result is an even number
number = (random.randint(1, 100))
print(random.randint(1, 100))
if number % 2 == 0:
    print(f"[number] is even.")
else:
    print(f"[number] is odd.")
# ---------------------------------------------------------------------
print("LOGIC & OPERATORS:")
# control flow and why we need it
# it's logic we build inside our code to control how it runs
# naturally python executes our commands step by step, from top to bottom
# but sometimes we have complex tasks hence the need to control the flow of our code
# the first way to control it is by building conditional statements
# we use it when we have two blocks of code but we don't want to execute both of them
# we want to execute one of them based on a question (condition) and based on the answer
# if the condition is True, we go to one block, if False, we go to the other
# we are building a logic, a decision
# so how a conditional statement works is:
# the statement is set and ran as 1 block of code, then if this block returns true, then we run ONE block of code, IF it's false instead another
# then the last block of code gets executed as normal as one block
# which means that at the end there's one whole block of code that did not get executed (either the True or False block following the conditional statement)
# it's like a crossroads in our code.
# but what if we want to keep repeating code until certain conditions are met?
# for that we create loops
# so essentially we start with the loop statement, then the loop
# if the loop returns one value then we go back to the beginning of the loop and repeat the process
# said process is repeated for aslong as the other condition requirements aren't met,
# once met the loop is gonna break and the rest of our code is gonna execute as normal
# ------------------------------------------------------------------------
print("CONTROL FLOW TOOLS:")
# Control flow statements: special instructions in python to change the flow
# 1) conditional statements: if - else - elif these help us make decisions
# 2) repeteated tasks aka loops: for - while
# we also have some control tools like: break - pass - continue
# the statements alone aren't enough though we need to give python conditions to evaluate
# Values = True or False booleans ("yes" or "no")
# logical operators: and - or - not
# membership operators: in - not in
# identity operators: is - is not
# -----------------------------------------------------------------------
print("\nBOOLEAN OPERATORS:")
# this function gives True because it checks wether the value is empty or not
print(bool(123))
print(bool("hi"))  # regardless of value type
print(bool())  # and here it returns False because it's empty
# 0 also returns False because in the boolean function it's considered as nothing
print(bool(0))
print(bool(""))  # this is also False for boolean functions and counted as nothing
# None isn't a empty value, it's considered a missing value: none = no value / empty = existing value but empty string
# Also turns False since None means it has no value so it's treated similarly to a empty string
print(bool(None))
# ----------------------------------------------------------------------
# for example: functions: bool() any() all() isinstance()
print("\n any/all/isinstance FUNCTIONS")
# if we have multiple booleans to return we can use any or all to returns them all together
# if lets say we have 3 booleans and atleast one is True the any function will return True
# while for all it will require all booleans to return True to return True itself
# EXAMPLE OF ANY:
email = ""            # if we had a website with the following rules:
phone = "33-21385645"  # allow registration: if any field is filled
username = ""         # any would return us True given these variables/values
# because atleast one value returns true, any also returns True
print("ANY:", any([email, phone, username]))
# ----------False---True---False
# if we however were to remove the one TRUE value we have then any would return False

# EXAMPLE OF ALL:
email = ""
phone = "33-21385645"
username = "Dani"
# all requires all booleans to return true which is why it returns, False in this case
print("ALL:", all([email, phone, username]))
# ---------False---True---True
# -----------------------------------------------------------------------
# isinstance(value, type) = built in function, outputs booleans
# checks if a value belongs to a certain data type
# checks the given value is of the specified data type, if it is returns True like this case
print("isinstance int:", isinstance(123, int))
# returns False because True is a boolean, not a str
print("isinstance str:", isinstance(True, str))

# isinstance can work similarly to endswith and startswith in the right circumstances
print("isinstance = endswith given this circumstance:", "hello".endswith("o"))
print("isinstance = startswith given this circumstance:", "hello".startswith("o"))
# -----------------------------------------------------------------------
# comparison operators: == - != < > >= <= used to compare two different values, the return is the boolean TRUE or False
print("\n COMPARISON OPERATORS:")
# in comparison operators we can compare and use: values 3 >2 = True
# variables: x = 5 - x < 2 = False
# expressions: 2-1 !=2 = True
# functions:len("hi") == 3 = False
# ----------------2---
print(4 == 4)  # returns True they are equals
# using != (not equal) returns False because 10 isn't different, it is in fact equal to 10
print(4 != 4)
print(5 > 3)  # True 7 is greater than 3
print(5 >= 5)  # True
print(3 < 5)  # True 3 is smaller than 5
print(5 <= 5)  # True 5 is equal OR smaller than 5
# True strings can also be compared since alphabetically they have a number assigned to them
print("a" < "b")
print("a" == "b")  # False because they have alphabetically different values
# reminder that python is case sensitive which is why a == A returns False
print("a" == "A")
# if we were to do "a" = "A" with = we are doing a assignment NOT a comparison, be aware, the return would be a syntax error
print(2 < 3 < 2)  # we can also chain operators just like in math, python executes chains from left to right and requires all comparisons to return True to return True
# so even if 2 > 3 returns True, 3 < 2 returns False which is why the whoe comparison returns False
age = 18
# chained comparisons are like SQL's between they check if a value is ebthween two bounds
print(16 <= age <= 29)
# ------True---True = True
# --------------------------------------------------------------------------------------
# and - or used to check the logic or the rule of our operatators, returns a boolean True/False
print("\nLOGICAL OPERATORS:")
# and = BOTH compared values need to return True for the comparison to return True
print(1 < 3 and 5 < 10)  # because both return true the result is true
# -----True------True--- = True
print(2 < 3 and 5 <= 4)  # Returns False because one comparison returns False
# -----True------False--- = False

# or = either of the compared values need to return True for the comparison to return True
# even if two comparisons return False, since one returns True = True
print(4 < 2 or 5 > 2 or 5 == 4)
# -----False-----True-----False--- = True
# even if two comparisons return False, since one returns True = True
print(4 < 2 or 5 > 6 or 5 != 5 or 4 == 4)
# -----False-----False-----False-----True = True
print(4 < 2 or 3 > 5 or 5 == 4)  # everything returns False = False
# -----False-----False-----False--- = False

# case scenario, to monitor a sistem that's under pressure
cpu_temperature = 54
memory_usage = 75
gpu_temperature = 63
# we want to know if ANY of them gets to critical levels
# because of that we use the or operator to check if/when any of them reaches these numbers, and return TRUE if they do
# telling us that we reached the critical area
print(cpu_temperature > 75 or memory_usage >= 75 or gpu_temperature >= 90)
# ---------FALSE----------------------TRUE--------------------False------ = TRUE

# case scenario: checking user credential before login, we use AND
email = True  # other examples can be ID, phone sent sms code, security phrase/word, backup Email code etc
password = True
username = False
phone = True
# because atleast one condition returns false the return is False
print(email and password and username and phone)
# -----True------True---------False---------True---- = False
# case scenario: checking if somebody can enter a venue
age = 30
has_ticket = True
is_member = True
is_vip = False
# because the last and requires either conditions bethween or to be True and one indeed is, it returns true
access_granted = age >= 18 and has_ticket == True and (is_member or is_vip)
# ------------------True---------------True------------------True-------False---- = True
# {access_granted} returns the boolean of the variable access_granted which is True in this case
print(f"Access granted: {access_granted}")
# --------------------------------------------------------------------------------------------------------------------------------
# not flips the truth, turns True into False and viceversa (uses boolean)
print("\nNOT OPERATOR:")
# commonly used in conditional statements and loops to check when a condition is not met.
print(3 > 2)  # obviously turns True
# but if we use the not operator we reverse the output and it turns False
print(not 3 > 2)
print(not True)  # what is not True? False
print(not False)  # what's not False? True
# we can also flip it twice which will just give you back the original value (so it's useless)
print(not not False)

name = ""  # boolean of empty is False
print(name)  # this will give out a empty string
print(not name)  # will turn True because the boolean of empty is false, so if we reverse it with not the outcome is glipped to True
# same here, because 0 is for a boolean False, not returns the flipped boolean True
print(not 0)

# use cases:
# User log in check
logged_in = False
if not logged_in:
    print("Please log in to continue")
# access control:
# if a user isn't a specific type or role of user, deny the access
user_role = False
if not user_role == "admin":
    print("Access Denied!")
# SEARCH UNTIL FOUND:
# in a loop use the not operator to search in a loop for a item until it is found
cars = ("BWM", "Ferrari", "Fiat", "Ford", "Suzuki", "Toyota")  # list of items
wanted_car = "Toyota"  # car(item) we are looking for
while wanted_car not in cars:  # loop that looks in the list for as long as the wanted item isn't found
    # updates us on the progress of the search
    print("Searching for the right car...")
else:
    print("Found!")  # tells us when the item from the list is found
    print(wanted_car)  # tells us the name of the item
# ---------------------------------------------------------------------------------------------------
print("\nCONTROL MIXED CONDITIONS:")
# and operator has a higher priority than the or operator, so python executes it first
# and is executed first and returns True and False = False
print(4 == 4 or 5 > 3 and 4 < 2)
# -----True------TRUE-----False
# but because right after we execute the or, and it returns True, it now has to deal with the False from the and = the True from the or, using the or = True

# if we want control over which operator is executed first we can use the pharentesis ()
# in this case with the () we force python to execute first the or, which returns True
print((4 == 4 or 5 > 3) and 4 < 2)
# -----True---OR----True = True - gets executed first because it's bethween paranthesis ()
# ----------True(or outcome)--------AND---False(and outcome) = False - and gets executed last and Returns False

# to recap, be careful of the order of the execution because it's important to determine the outcome of it.
# EXERCISE:
# allow access if user is logged in
# or if they are guests
# but they must not be banned
is_logged_in = True
is_guest = False
is_banned = False
# and is executed first returning False, False is Executed with the or operator together with True, returning True
print(is_logged_in or is_guest and not is_banned)
# -----True------or(executed last)------False------and not(executed first)------True
is_logged_in = True
is_guest = False
is_banned = True
# executes the or first returning True, turns to the and operation which, because it turns False, returns False
print((is_logged_in or is_guest) and not is_banned)
# --------True---or(executed first because ())----False------and not(executed last)--------True = False
# ------(True-------OR------False) executed first because of the ()
# --------------True-------and not------False = True and False = False
# ----------------------------------------------------------------------------------------------
# in operator checks wether a value is inside or not present in another value (can be str, list, tuple or other sequence) returns a boolean
print("\nMEMBERSHIP in:")
# case use: To look for the presence or the absence of a specific: date, year, name, brand etc within a database.
# IN used to check if the value is within the data, NOT IN to check when it's not present within the data
names = ["Dan", "Rob", "Luca", "Cri", "Emma",
         "Anna", "Jesse", "Davide"]  # list of variables
# checks the variables for the presence of the requested value and doesn't find it returning False
print(f"Tim in names = ", "Tim" in names)
# returns false because the value is present
print(f"Davide not in names = ", "Davide" not in names)
# returns True because Luca is present within the given variables
print(f"Luca in names = ", "Luca" in names)
print(f"1990 not in [1991,1992,1993,1994,1995] = ", 1990 not in [
      # returns True because 1990 isn't present within that list
      1991, 1992, 1993, 1994, 1995])

# case use: ensure the domain is not banned
domain = ["gmail.com"]
banned_domains = ["spam.com", "fake.org", "bot.net"]
# returns true because gmail.com isn't in the banned domain list
print(f"domain not in banned_domains = ", domain not in banned_domains)
# we can use the in operator to build quality checks aswell as security checks.
# --------------------------------------------------------------------------------------------------------------
# identity(is) operator checks if two variables refer to the same object in memory, returns a boolean
print("\n IDENTITY OPERATORS: IS/IS NOT")
# while variables such as a=[1,2,3] and b=[1,2,3] have the same list values, while stored in memory they have a specific id, unique to them
a = [1, 2, 3]
b = [1, 2, 3]
# if we were to compare lets say a =[1,2,3] and b = [1,2,3]
# True because it would compare the values of the variables
print(f"a == b =", a == b)
# if we were to use the is operator, while stored in memory the id of a = 30(example) b = 40(example) henche they are not the same
print(f"a is b =", a is b)
# False because while stored in memory the id of a = 30(example) b = 40(example) henche they are not the same
print(f"a is not b =", a is not b)
# if however we store one single value, that value, will be sored with a single id which means:
a = "Ada"
b = "Ada"
print(f"a == b = ", a == b)
# that because id wise, Ada is stored in memory with a single id, then the operator is will recognize a and be to be the same.
print(f"a is b = ", a is b)
# what happens if we assigne one variable to be equal to another?
a = [1, 2, 3]
b = a
print(f"a == b = ", a == b)
# for the b python in memory isn't creating a new object id so the result is True because the variables of a use the same id as those of b
print(f"a is b = ", a is b)

# make sure the email existsand is filled and is not empty:
print("CASE USE: make sure the email exists and is filled and is not empty:")
email = ""
print(email)  # would return True

email = "dani.@gmail.com"  # lets assume this is the user's input, a blank
print(email != "")  # True

email = None
# we generally use the is operator instead of the == operator when checking for None
print(email != None and email != "")
# ---------False------------True---- = False
email = None
print(email is not None and email != "")
# ----------------------------------------------------
