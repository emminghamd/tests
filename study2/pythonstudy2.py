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

phone = "176-1243-43"  # here we want to separate - with a /
print(phone.replace("-", "/"))
print(phone.replace("-", ""))  # or with nothing (kind of like removing the -)
print(phone.replace("-", " "))  # or with a character such as space

price = "$1,299.99"  # what if we want to do multiple changes?
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
print("\nRANDOM:")  # random: random() randint()
# random function - returns float - returns a random float bethween 0.0 and 1.0
print(random.random())
# what if we want to roll a random integer (for example rolling a dice or selecting a random name from a list)
# generates a random number bethween two given numbers
print(random.randint(1, 10))
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
print(any([email, phone, username]))
# ----------False---True---False
# if we however were to remove the one value we have then any would return False

# EXAMPLE OF ALL:
email = ""
phone = "33-21385645"
username = "Dani"
# all requires all booleans to return true which is why it returns, False in this case
print(all([email, phone, username]))
# ---------False---True---True
# -----------------------------------------------------------------------
# isinstance(value, type) = built in function, outputs booleans
# checks if a value belongs to a certain data type
# checks the given value is of the specified data type, if it is returns True like this case
print(isinstance(123, int))
# returns False because True is a boolean, not a str
print(isinstance(True, str))

# isinstance can work similarly to endswith and startswith in the right circumstances
print("hello".endswith("o"))
print("hello".startswith("o"))
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
# -------------------------------------------------------------------------------
# a checkpoint in our code, if the condition is True it will run the code, if False it will do something else
print("\nCONDITIONAL STATEMENTS:")
print("\nIF Statement:")  # used to define the first condition
# rules: 1) there can only be one if in a statement
# 2) a if statement must start with an if
# 3) the if statement is required, not optional
# 4) it can stand alone
score = 100  # set a value
# start a condition, and a parameter to evaluate, also be aware that a statement must allways end with : (double point)
if score >= 90:
    print("prints if the condition in the statement is True")
    # the print above is a intendation.
# an indentation is when you add spaces at the start of a line to show that the line belongs to a code block
# --------------------------------------------------------------------------
print("\nINDENTATION:")
# When a line (or multiple lines) belongs to another line python first runs the line that the intended line belongs to (in the example above that would be the if statement)
# so taking the above example it means that if the IF statement were to not turn True, we'd skip the intended lines belonging to it.
# we can also nest stuff inside eachother:
# def check_event(number): # main statement
#   if number % 2 == 0: # nested statement belonging to the def statement
#      print("even number") # intentation to if statement
#   else: # other nested statement belonging to the def statement
#      print("odd number") # indentation belonging to the else statement
# -------------------------------------------------------------------------------
# runs if only all previous conditions in the statement are False
print("\nELSE: two way condition")
# there is no scenario where we execude both or neither parts of the code:
# if we have a if statement and a else statement, we either end up executing the IF statement (if True) or the else statement (if False).
# the else statement must allways come at the end and doesn't contain any conditions itself
# it's also completely optional but it can not stand alone, it allways needs an if
# cannot have multiple else statements in the same chain
# practica example:
age = 18  # sets the value of the variable
if age <= 17:  # asks for a value that's not within the given value so the if is skipped
    print("too young")
else:  # the previous statements are skipped henche the else statement gets returned
    print("of age")
# -----------------------------------------------------
# asks a follow up question that runs only if the previous statements were False
print("\nELIF: multiple conditions")
# "if the first wasn't true try this one"
# if condition1: do A - elif condition2: do C - else: do B
# in a conditional statement we can: run a if statement as the "False statement instead of Else", we can run multiple initial if statements using and/or operator
# we can also run independent if - check for independent if further down this file
# the elif comes allways after the if statement/s.
# you can use as many elif blocks as you want (not a rule just a bonus), aslong as it follows the rules
# like the if statement a elif statement also needs a condition
# it's optional and it cannot stand alone, if included, it must follow a if statement
print("Branching elif")
temperature = 26  # value
if temperature is 25:  # if statement asking for a value above a range
    print("Perfect weather!")
elif temperature >= 16 and temperature <= 35:  # two different elif statements that cover a specific range
    print("nice weather")
elif temperature >= 36:  # elif that covers any range past a certain point
    print("it's hot")
else:  # if the previous statements are skipped returns this
    print("it's cold")
# ------------------------------------------------------------------
# if statements inside other if statements = if this is True, then check the next
print("\n NESTED CONDITIONS: ")
# nested if statements can have a else added to it
score = 91
submitted_project = False
if score >= 90:
    # nested condition we don't need to do comparisons with = because python evaluates booleans directly.
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# -----------------------------------------------------------------------
print("\nCONNECTING CONDITIONS: using logical operators and/or ")
score = 91
submitted_project = False
if score >= 90 and submitted_project:  # logical operator and used to check if both conditions turn True
    print("A+")
elif score >= 90:  # A is returned because the if with the and doesn't return two True.
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 51
submitted_project = True
if score >= 90 and submitted_project:  # logical operator and used to check if both conditions turn True
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
# returned because even if we don't have the score at 60+ we do have the project set to True
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")
# --------------------------------------------------------
# a if statement that comes after another if statement and acts completely independently
print("\nINDEPENDENT IF:")
score = 91
if score >= 90:
    print("High score")
else:
    print("Low score")

submitted_project = True
if submitted_project:
    print("project submitted")
else:
    print("project missing")
# ---------------------------------------------------------------------------------------------

# we can make a inline statement completed with if, else statements if we want:
print("\nINLINE IF (TERNARY):")
# the correct syntax would be to write the condition before the statement itself
# we also cannot use the elif statement, and the function must have both if and else in it.
# the other thing to note is that the result of this inline statement is gonna be stored in a variable:
# x = "A" if score >= 90 else "F"
# the tradeoff is that inline statements can only be used if their logic is really simple since they can run only that one if and else statements
# example:
score = 60  # we still need to give a value to the variable we want to check
# this is how we'd normally write a if statement:
# if score >= 60:
#     print("Passing")
# else:
#      print("failes")
print("Passing" if score >= 60 else "Failed")  # can be simplified like this
age = 25
print("Access granted" if age >= 18 and age <=
      25 else "Access denied")  # can also use and/or

temperature = 25
# transformed the statement's outcome variable into a value
degree = "Hot" if temperature >= 25 else "cold"
print(degree)

# how can we add a elif in here? by adding multiple if statements like so:
print("\ninline alternatives to elif: multiple if")
grade = 60
grade = "A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "D" if grade >= 60 else "F"
# var----------1 if 90+-------------2 if 80+------------------3 if 70+-----------------4 if 60+------else 59 or less
# each if needs a else and the last else should hold the last value
print(grade)
# can also type it within multiple lines if we envelop it in pharentesis to make it more readable
grade = 60
grade = ("A" if grade >= 90
         else "B" if grade >= 80
         else "C" if grade >= 70
         else "D" if grade >= 60
         else "F")
print(grade)
# but one should avoid using inline statements for very complex statements as it would be very hard to read
# -------------------------------------------------------------------
# evaluate va value against multiple possible values runs the code of the first match
print("\nSPECIAL STATEMENTS: MATCH CASES: ")
# case example: we want to convert full country names into two letter abbreviations
country = "USA"
if country == "United Kingdom":
    print("UK")
elif country == "United STATES":
    print("US")
elif country == "Italy":
    print("IT")
elif country == "Netherlands":
    print("NL")
else:
    print("unknown country")
# we could use match to make the code more readable like:
match country:
    case "United Kingdom":
        print("UK")
    # we can pipe and add multiple matches if we want/need to like such:
    case "United States" | "USA":
        print("US")
    case "Germany":
        print("DE")
    case "Netherlands":
        print("NL")
    case "Italy":
        print("IT")
    case "France":
        print("FR")
    case "Australia":
        print("AU")
    # _: = if none of the above matches, execute this (kind of like a else statement)
    case _:
        print("Invalide Country")
# it's important to remember though that match can only be used for matching values
# ----------------------------------------------------
# a tool used to repeat a code block until a condition is met/isn't met anymore
print("\nFOR LOOPS:")
# useful for when we need to repeat the same code multiple times, we could jsut put it in a loop and repeat it for aslong as we need
# goes through a group of items one by one to do something for each item
print("FOR LOOP:")
# for loop structure: for i in (1,2,3) in the intended line afterwards we could have print(i) which will execute print(i) for 1, then for 2 then for 3 and finally will get us out of the loop
# i is the variable (1,2,3) the sequence, group of items that should be iterated, python goes and creates in the memory a "iterator" out of it.
# a iterator is responsible for knowing what's done and what's next
# the print instead is the code to be repeated that until the iterated list has been processed.
# the things we can sequences are: tuple (sequence of numbers), lists (sequence of items can include str), str (sequence of characters), range, dict, file aslong as they are iteratable
# example of tuple:
for i in (1, 2, 3, 4, 5):  # i is the variable, (1,2,3,4,5) the tuple sequence
    # this print the operation to repeat untill the whole sequence has been resolved.
    print(f"rounds: {i}")

# we can also create the sequence outside the for loop and call the singular objects in said sequence using the singular, while the list using plural
# for example name (singular value) names (sequence) or number(singular value) numbers (sequence)
names = ("Daniel", "Colin", "Elvis", "Bob", "Anne", "Phyllis")
for name in names:
    print(f"name: {name}")
# example of list:
items = [1, 2, 3, 4.4, "ok"]
for item in items:
    print(f"item: {item}")
# example of str
letters = " Python"  # even the spaces will be executed as individual parts of the sequence
for letter in letters:
    print(f"letter: {letter}")
# example of range
for number in range(5):
    print(f"range item: {number}")
# as we know python starts counting from 0 and by default stops before the given number, which means here 5 isn't included
# to change this if for example we didn't want 0 included and we wanted 5 included:
# range(5) -> range(1, 6) = the first value here is called the start (if not called it's defaulted at 0) argument, the second the stop argument = range(start, stop)
for number in range(1, 6):
    print(f"start/finish item: {number}")
# the last argument we can add is the optional argument step: round(start, end, step)
# used to define or specify the incrementation, if not included it defaults to +1
for number in range(1, 10, 2):  # counting all the odd numbers bethween 0 and 10
    print(f"incremental by odd item: {number}")
for number in range(2, 10, 2):  # counting all the even numbers bethween 0 and 10
    print(f"incremental by even item: {number}")
for number in range(2, 10, 4):  # the steps can obviously be bigger
    print(f"incremental by 4 item: {number}")

# REAL WORLD EXAMPLES:
# if we have big taples of data that we'd like to move, we could write them over one by one or we could use a loop to iterate through all tables to move them all.
# we can also use the loop to go through files and clean them up, for as long as this is the same action/s a loop could handle it for us.
# we can also iterate through columns (exel spreadsheet for example), we could have leading of trailing spaces, so we could use a loop with the strip function to cleanse these
# we also use loops to go through data and do: aggregations, summing, counting or averaging.
print("Real world example 1: summing up the variable's values")
scores = [80, 50, 60, 75]  # variables
total = 0  # final result we are adding variables to
for score in scores:
    # as the loop runs it adds the variables (score) to this total
    total += score
    # at every variable iteration writes the new total
    print("Current Total:", total)
# once the loop is over gives us the final total of all the variables added together
print("final total:", total)
print("real world example 2: cleansing/replacing values")
# inconsistent casing/spaces to fix
# lets say we want to get rid of the txt files and replace them with our new standard scv:
files = [" File.csv ", "DATA.scv ", " final.TXT "]
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    # strip() = strip spaces from front/rear - lower() = convert upper to lower case letters - replace("", "") = replace a certain part of the variable with something else
    # it's important to first clean up the data and then do data transformation (if we did replace before lower, it wouldn't work)
    print(f"processing: {file}")
# for more examples/exercises check the forloopexercise.py file
# -----------------------------------------------------------------------------------------
print("\nBreak/continue/pass: control statements")
# break = immediatly stops the loop
# for example if we set a for loop with a few numbers, lets say (1,2,3) and we make a if statement that says, when i == 2: break,
# then our loop would execute 1, execute 2 which turns true and because of that we break out of the loop
# and continue through the rest of the code while not even bothering to check 3
print("break statement example")
names = ["ada", "jon", "emma", "", "Anna", "luca"]
for name in names:
    # sets out condition for the break to get us out of the loop resulting in "" (empty value), Anna, Luca not being shown (since they come after)
    if name == "":
        print("name missing")
        break  # must be intended to a if if we want to avoid breaking out from the loop from the first iteration
    # prints the values up to the if value that has the break condition
    print(f"name = {name}")
# use scenario: we use break to get out of the loop once the data we want to extract has been found
# -----------------------------------------------
# continue = skips one loop cycle without stopping the loop, so with the example of (1,2,3) above,
# python would execute 1 and 3 but it will skip executing 2 because that one falls true under the continue condition
print("\n continue statement example:")
cars = ["bwm", "fiat", "renault", "", "ford", "toyota"]
for car in cars:
    if car == "":  # selects the value, which we will skip with the continue statement
        continue  # skips the value we chose with the if statement
    # prints the whole list without the one we skipped using continue
    print(f"car brand = {car}")
# use scenario: we use continue to skip bad or empty data without stopping a loop
# --------------------------------------------------------------------------------
print("\npass statement example")
# pass = for now do nothing, we use it as a placeholder while coding
# with the example of [1,2,3], if pass was used on the two, 2 would still be
indexes = (1, 2, "a", 3, 4)
for index in indexes:
    if index == "a":  # we execute this anyway with pass but have setup the code for maybe coming back to change things
        pass  # executes the if statement value, just acts as a placeholder for modifications to the code we might do later
        # example of a possible fix could be:
        # index = index.replace("a", "unknown")
    print(f"index = {index}")
# use scenario: we use pass when we aren't sure what to do yet with a value and need to decide what to do with it.
# for more example/exercises of continue/break/pass check the forloopexercise file
# ----------------------------------------------------------
