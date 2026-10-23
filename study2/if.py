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
