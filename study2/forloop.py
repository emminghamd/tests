# a tool used to repeat a code block until a condition is met/isn't met anymore
print("\nFOR LOOPS: tuple, sequence/singular values, list, str, range")
# useful for when we need to repeat the same code multiple times, we could jsut put it in a loop and repeat it for aslong as we need
# goes through a group of items one by one to do something for each item
# for loop structure: for i in (1,2,3) in the intended line afterwards we could have print(i) which will execute print(i) for 1, then for 2 then for 3 and finally will get us out of the loop
# i is the variable (1,2,3) the sequence, group of items that should be iterated, python goes and creates in the memory a "iterator" out of it.
# a iterator is responsible for knowing what's done and what's next
# the print instead is the code to be repeated that until the iterated list has been processed.
# the things we can sequences are: tuple (sequence of numbers), lists (sequence of items can include str), str (sequence of characters), range, dict, file aslong as they are iteratable
print("\ntuple:")
for i in (1, 2, 3, 4, 5):  # i is the variable, (1,2,3,4,5) the tuple sequence
    # this print the operation to repeat untill the whole sequence has been resolved.
    print(f"rounds: {i}", end=" ")

# we can also create the sequence outside the for loop and call the singular objects in said sequence using the singular, while the list using plural
print("\nname (singular value) names (sequence) or number(singular value) numbers (sequence):")
names = ("Daniel", "Colin", "Elvis", "Bob", "Anne", "Phyllis")
for name in names:
    print(f"name: {name}", end=" ")
print("\nlist:")
items = [1, 2, 3, 4.4, "ok"]
for item in items:
    print(f"item: {item}", end=" ")
print("\nstr")
letters = " Python"  # even the spaces will be executed as individual parts of the sequence
for letter in letters:
    print(f"letter: {letter}", end=" ")
print("\nrange:")
for number in range(5):
    print(f"range item: {number}", end=" ")
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
print("\nsublist:")  # sublist operator
# we can also make a sublist of a list using a different operator : instead of ,
# example: we want to extract only 1 value every 2 for downsampling:
list = [10, 20, 30, 40, 50, 60, 70]
# [start:end:step] - if we omit start = 0, if end = full list - if we omit step we simply don't skip.
for item in list[1:7:2]:
    print(item, end=" ")
# this is useful if we want to do a downsampling of data


# REAL WORLD EXAMPLES:
# if we have big taples of data that we'd like to move, we could write them over one by one or we could use a loop to iterate through all tables to move them all.
# we can also use the loop to go through files and clean them up, for as long as this is the same action/s a loop could handle it for us.
# we can also iterate through columns (exel spreadsheet for example), we could have leading of trailing spaces, so we could use a loop with the strip function to cleanse these
# we also use loops to go through data and do: aggregations, summing, counting or averaging.
print("\nReal world example 1: summing up the variable's values")
scores = [80, 50, 60, 75]  # variables
total = 0  # final result we are adding variables to
for score in scores:
    # as the loop runs it adds the variables (score) to this total
    total += score
    # at every variable iteration writes the new total
    print("Current Total:", total, end=" - ")
# once the loop is over gives us the final total of all the variables added together
print("\nfinal total:", total)
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
    print(f"index = {index}", end=" - ")
# use scenario: we use pass when we aren't sure what to do yet with a value and need to decide what to do with it.
# ----------------------------------------------------------
# so to recap:
# break is used to stop the loop immediatly, useful for critical risks: cost - security - integrity
# continue: skips a single instance not everything: medium risks: bad rows - empty data - skip special cases
# pass: placeholder code for something we want to decide what to do about later
# for more example/exercises of continue/break/pass check the forloopexercise file
# --------------------------------------------
print("\n FOR ELSE LOOPS:")
# else used in for loops executes once we finish the whole loop
# else used simply with IF either choses True or False in which case returns the else statement
# example:
items = [1, 2, 3, 4]
for item in items:
    print(f"{item}", end=" ")  # prints the list in a line
# else: # this else could be absent and nothing would change, the print afterwards would be executed regardless
    # print("if/else example")  # prints this
# there is only one scenario in which a else statement makes sense, and that's to use it with "break"
# to end a loop that would otherwise be endless or would or would otherwise process things we don't want processed.
# example of else: break
items = [1, 3, 4, 5,]
for item in items:
    if item % 2 == 0:
        print("even number found:", item, end=" ")
        break
    else:  # else will be ran only if the loop doesn't get interrupted by the break
        print("all the numbers are odd")
# real case scenarios: we use for else loops to search and validate our data whether good or bad.
# example: in the following we look for a invalid name and stop the loop if we do (to avoid problems)
names = ["Luca", None, "Anna"]
for name in names:
    if name is None:  # if we find the invalid entry
        print("invalid name")  # send this message
        break  # and break out of the loop
else:  # else validate our values
    print("validated names)")
# other example: file extension validation:
files = ["report.csv", "bot.pdf", "data.csv", "img.gif"]
for file in files:
    if not file.endswith(".csv"):  # if the unwanted file type is found
        print("invalid file types")  # print
        break  # break out of the loop
else:  # otherwise print the following
    ("validated file types")
# --------------------------------
print("\nNESTED LOOPS:")  # loop inside another loop
# outerloop starts when it gets into the innerloop it processes it (and any further nested loops inside) before going back to the outer loop
# example: outerloop with values 1,2,3 innerloop with value 1,2 =
# outerloop first value + innerloop values = 1,1 and 1,2
# outerloop second value + innerloop values = 2,1 2,2
# outerloop third value + innerloop values = 3,1 3,2
# no more outerloop values = loop is completed
# example:
for x in range(3):  # outer loop
    for y in range(2):  # 1st inner loop
        for z in range(2):  # 2st inner loop
            print(f"({x},{y},{z})")
# ------------------------------------------------------------------
# CASE SCENARIOS: crossing data (between different files for example):
# make a catalog with all color and sizes
colors = ["Blue", "Red", "Green"]
sizes = ["Small", "Medium", "Large"]
for color in colors:  # iterating the variable colors
    for size in sizes:  # iterating the variable sizes
        print(f"({color}, {size})", end=" - ")
# this is what we call cartegians, cross or compiling the data
# -----------------------------------------------------------------------------
# CASE SCENARIO: going through layers or "navigating the hierarchy"
# lets say we have to create multiple reports:
# for each year, for each month, for each day

years = [2026, 2027]
months = ["oct", "nov"]
# for simplicity's sake we are limiting the amount of days
# also because of the fact that 3 isn't considered in the range,
# remember that if we wanted to do this with 31 days
# we'd have to write range(1,32) to include the 31
days = range(1, 3)
for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}_csv", end=" ")
# -----------------------------------------------------
# CASE SCENARIO: navigating through tables and columns and rows
tables = 2
columns = 2
rows = 2
for table in range(tables):
    for column in range(columns):
        for row in range(rows):
            print(f"table:{table} - column:{column} - row:{row}", end=" ")
# --------------------------------------------------------------------------------
print("\nWHILE LOOPS:")
# used to repeat a block of code over and over for aslong as the condition is TRUE
# difference bethween for loop and while loop:
# in for loop we are pre-defining the iterations and we also know already how many times we will iterate
# in a for loop also the item we are iterating everytime
# in a while loop instead we are working with the assumption that a condition that WE define is True(bol), and we loop out as soon as it turns out False(bol)
# in a while loop we also don't know up front how many loops it will take to get out of the loop
# so, in a for loop we iterate over a sequence like: list, range, toupe, dictionary, a known value
# and, with a while loop we are iterating over a condition that could change any time (and that we can choose)
# this also means that a while loop is prone to potentially run infinitly, which we need to be careful/aware of.
# so we have two types of while loops:
print("\nWHILE CONDITION: given a condition the loop is able to break out of the loop")
print("\nexample of using a update to break out of a loop")
i = 1  # initialization
while i <= 3:  # condition
    print(i, end=" ")  # print
    i += 1  # update (allows us to get out of the loop)
print("the update can function like a step, for example we could make it give us a step of 2:")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 2
print("example of asking input as a way to get out of a loop:")
user_input = ""  # empty because we get this value from the user while in the loop
while user_input != "yes":  # accepts only yes, goes infinitly if we don't add a way out of this
    # with this we add the possibility to change the value so that the user can get out of the loop
    user_input = input("type: (yes/no): ")
print("welcome in user")
# use scenarios: when we need to add a counter, limit retries (like for example limit the password attempts)
# --------------------------------------------------------------
print("\nWHILE TRUE: ")
while True:  # infinite loop while true
    user_input = input("please say: (yes/no)")
    if user_input == "yes":
        break
print("thanks")
# use case: we have a open ended scenario and we are waiting for a external trigger:
# database, stream, API
# to recap: while conditional is safer and more readable
# while True must have a if + break and has risks of infinite loops but is more flexible
# try to use while conditional if/when possible as it's much safer and easier to read/use
# ---------------------------------------
print("\n Difference bethween For loop and while loop:")
# FOR LOOP: works over a fixed sequence
# has predefined conditions
# the number of iterations is known
# PRO: simple, clear, safe CON: limited
# WHILE LOOP: loop while a condition is True
# uses your condition
# number of iterations is unknown
# PRO: advanced, flexible CON: complex, risky (due to infinite loops etc)
# -------------------------------------------------------------
