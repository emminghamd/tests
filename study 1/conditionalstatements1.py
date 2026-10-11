print("CONDITIONAL STATEMENTS")
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
LOGICAL OPERATORS: and - or - not""")
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
