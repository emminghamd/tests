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
#   print("ECHO", command)  # echoes our result
# .lower allows us to check for quit with all variations of lower/upper case letters
# command = input(">") stores the new data for us in command
# the in-built terminal is read only which won't work for this command
# run this in the normal terminal wirting:  python3 filename.py (name of the file)


print("""
INFINITE LOOPS""")
# while True:  # having a infinite loop means we don't need to define command and setting it to a empty string
#    command = input(">")
#    print("ECHO", command)
#    if command.lower() == "quit":
#        break
# because the command runs forever for aslong as it's True we need to add a if statement (in this case with quit) with a break so that IF we type that word we break out of the loop
