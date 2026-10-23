print("\n LAMBDA") # function
# tiny function without a name also called anonymous function
# used often with map, filter sorted
#example:
num = 2
multiply = lambda x: x * 2
print("number we chose:",multiply(4)) 
print("pre-defined value:",multiply(num)) 
# value in the parenthesis can either be one we chose or one we defined
#----------------------
num1 = 4
num2 = 3
two = lambda x, y: x + y # hewe we determine two values 
print("addition between numbers we chose: ",two(2,5))
print("addition between pre-defined values:",two(num1, num2))
#-------------------------------------
# lambda can contain only one expression but can return mulltuple results combining them into a tuple:
calc = lambda x, y: (x + y, x- y, x * y, x / y)
res = calc(4,2)
print("\n one expression multiple tuple outcomes:",res)
# one expression, tuple with multiple results: addition, subtraction, multiplication, division
#----------------------------------------
# using lambda to check for occurrances of characters
check = lambda i: i in "python" # checking if a value is within our str
print("\nchecking character presence:",check("z"))
# returns false because z isn't present without the str python
#--------------------------------------
name = ("Dani")
cap = lambda x: x.capitalize()
# upper is the new declared value that comes off the magda function, x calls to whatever we want (name in this case) and .capitalize is what we chose to do with our variable to change
print("Capitalize: ",cap(name))
#-----------------------------------------------------------
# example: we need to convert the prices below to a float first then we can work with them:
print("\nlambda can use the conditional expression if-else to return different results based on condition")
numbers = [3,-4,0]
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(numbers[0])) # variable + index
print(check(numbers[1])) # variable + index
print(check(numbers[-1])) # variable + index
#--------------------------------
# lambda if-else can also be used to check for even/odd numbers given specific conditions
numbers = [1,5,3,6]
even_odd = lambda x: f"{x} is even" if x %2==0 else f"{x} is odd"
print(even_odd(numbers[0]))
print(even_odd(numbers[-1]))
#----------------------------------------------------------
print("\nMAP + LAMBDA: ")
# lambda + map = lambda applies a expression to each list elements, map iterates through the list and applies the transformation
numbs = [1, 2, 3, 4]
tenpercent = map(lambda x: x * 2, numbs)
print("\nmultiplying each value within a list",list(tenpercent))
# doubling every given number in value
#--------------------------------------------------
numbs = [1, 2, 3, 4]
tenpercent = map(lambda x: x * 1.1, numbs)
print("\n10% increase to each value within a list",list(tenpercent))
# obtaining 10% increase to each given number
#---------------------------------------------------------------------------
# instead of writing the following for all values we will use a lambda for it
prices = ["$12.50","$99.99","$100.00"]
# p = "$12.50"
# print(float(p.replace("$", "")))
print(map(lambda p: float(p.replace("$", "")),prices))
# list to convert it so it's readable
print(list(map(lambda p: float(p.replace("$", "")),prices)))
# map function to be able to repeat the lambda function for all values in the list
#--------------------------------------------------------------
print("\nFILTER + LAMBDA")
# lets say we want to show only numbers above 100
prices = [30, 150, 300, 80]
print("filter out numbers below 100",list(filter(lambda p: p > 100, prices)))
#------------------------------------
# nested list examples:
# we want to exclude anybody that didn't get atleast 60 points
students = [["Ella", 58],
        ["Rob", 74],
        ["Dani", 84]]
print(list(filter(lambda row: row[1] > 60, students)))
# we named it row only to make it obvious for what it is
# that row[1] targets the number (the name would be 0) so that we can then check for scores that are higher than 60 and show them
#------------------------------
# keep only people that have their name starting with a certain letter using startswith or row [][]
students = [["Ella", 58],
        ["Rob", 74],
        ["Ross", 84],
        ["Emma", 78]]
print("names starting with E:",list(filter(lambda row: row[0][0] is "E", students))) # checking by first value
print("names starting with R:",list(filter(lambda row: row[0].startswith("R"), students))) # using startswith
#------------------------------------------------
# lambda selects elements from the list that fulfill the condition
# filter filters out the unwanted ones
c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print("\neven numbers:",list(even))
# filtered out odd numbers from the list
#--------------------------------------------------
c = [1, 2, 3, 4, 5, 6]
odd = filter(lambda x: x % 2 != 0, c)
print("odd numbers:",list(odd))
# filtered out even numbers from the list
#-----------------------------------------------------------
print("\nSORTED + Lambda")
# we can use lambda to also sort by values within  a matrix, in this case lets sort by age and by alphabetical number
students = [("Luca", 5),
            ("Saskia", 22),
            ("Frank", 28),
           ("Albert", 18)]
# sorted by youngest to oldest
print("sorted list:",sorted(students, key=lambda x: x[1]))
# sorted by the name in alphabetical number
print("sorted list:",sorted(students, key=lambda x: x[0][0]))
