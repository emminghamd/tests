print("\n LIST COMPREHENSION:")
# a list comprehension is a way to write shorter syntax when you want to create a new list based on values from a preexisting list.
# when using it you have a structure: 
# data transformation, loop, data filtering
# we can either divide these by 1 space or put them like below in different lines for readibility purposes
#------------------------------------------------------------
# EXAMPLE: we want to clean up the following:
# 1) case sensitivity (upper) 2) www. 3) data without domain
domains = ["www.google.com", 
           "openai.com",
           "localhost",
           "WWW.FAKEBOOK:COM"]
# to do this we create a cleaned variant of this list: and inside we:
# data transfomr / loop / filter data
cleaned = [
           d.lower().replace("www.", "") # data transformation
           for d in domains # for loop
           if "." in d # data filtering (optional) 
] 
# with data transformation we get rid of upper/lower case incongruencies
# and we replace www. with nothing
# the for loop iterates through the list for us
# the if filters out bad data
print("looped through a list to transform and filtered data: \n",cleaned)
# but you can also skip some parts:
# 1) data transformation
nofilter = [
           d.lower().replace("www.", "") # data transformation
           for d in domains # for loop
] 
print("no filter: \n",nofilter)
# in this example we transformed data but we didn't esclude the bad data
# 2) data filtering
nofilter = [
           d # we need to define d but we just declare it and don't transform any data
           for d in domains # for loop
           if "." in d # data filtering (optional) 
]
# for any list comprehensions we could also just write it in one line:
# just need to make sue there's a space between the data transformation, loop and filtering.
# nofilter = [ d  for d in domains  if "." in d]
print("no filter: \n",nofilter)
# this is useful if all we want to do is filter out bad data and we are content with the rest of the data itself
# EXAMPLES:
#------------------------------------------------------------------
# square every number in a list:
nums = [4,5,6,8] # defining list
res =[val ** 2 for val in nums] 
# val**2 is the data transofmration
# for val in nums the loop
# we have no data filtering
print("\nsquare number of variables in list:",res)
#--------------------------------------
# create a new list to filter from a existing one all even numbers
n = [1,2,3,4,5,6,7]
even = [val for val in n if val % 2 == 0]
# val at the start is us defining the variables BUT not transforming it
# for val in n our loop
# i val % == 0 is us finding which variables within the original loop are even
print("even numbers:\n", even)
#same but for odd values now
odd = [val for val in n if val % 2 != 0]
print("odd numbers:\n", odd)
#---------------------------------------------
num = [5,3,9,42,53,4,11,21]
greater_than = [val for val in num if val > 10]
# val defining variable
# for val in num our loop
# if val > 10 us finding values higher than our wanted number
print("greater than 10:\n", greater_than)
#-------------------------------
# creating a list of numbers within a range
a = [i for i in range(10)] # i is variable for in in range loop
print("list of numbers within a range:\n",a)
#-----------------------------------------------------
a = [i for i in range(4, 10)]
print("list of numbers within a range with a start, end",a)
#-----------------------------------------------------------
# example of a list of coordinates obtained by combining two lists inside a list comprehension:
coordinates = [
           (x, y) # our varialbes
           for x in range(3) for y in range(2) # 1 loop for each coordinate
]
print("list of coordinates obtained by combining two lists:\n",coordinates)
#------------------------------------
print("\ntransforming a matrix worth of varaibles into one single list")
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("original matrix:\n",mat)
one_list = [val # val is our variable we need defined
            for row in mat for val in row]
# for row in mat selects each row
# for val in row selects each value in each row
print("single list of all items from all rows in the matrix\n",one_list)
#-------------------------------------------------------