# way of storing data so it can be used efficiently
import copy
print("DATA STRUCTURES: list[] - tuple() - set{} - dict {}")
# it's a way of avoiding the use of declaring multiple values ending up with a messy and lenghtly code
# example, the following:
cost1 = 10
cost2 = 15
cost3 = 20
cost4 = 25
total_cost = cost1 + cost2 + cost3 + cost4
# can be simplified like so:
costs = [10, 15, 20, 25]  # list
print(sum(costs))  # sum of the values in list
# list [1,2,3] - collection of variables you can order, change and duplicate these variables
# tuple (1,2,3) - the variables inside are unchangable
# set {1,2,3} - variables are unique = can't have variable duplicates inside a set
# dict {"a":10, "b":20, "c":15} - key value pairs = key = value / fondamental for data analyst/engineer/scientist

# what can we do with something like a list:
# we can find a specific data and read it, or we can change it, or we can search for bad data, and we can also transform data

print("\n difference bethween functions and method:")
# a function takes a input and gives a output
# a method takes a input, changes it but returns None, nothing
# -------------------------------------------------------------
print("\nhow to create a list: ")
print("manually creating a list")
empty = []  # if we leave a list empty
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
# list is the type and in the memory python goes and creates the variable for each object as a str if it's a str "a" as a int etc
mixed = [1, "a", True, None]  # int, str, bool, None
print(numbers)
print(type(numbers))

# converts a iterable (sequence) into a list
print("adding the datatype list()")
empty = list()
print(empty)
letters = list("Python")  # list of letters that compose this str
print(letters)
numbers = list(range(5))  # list of numbers
print(numbers)

print("nested list(matrix")  # we can make a list in a list to create tables
matrix = [["a", "b", "c"],
          ["d", "e", "f"]]  # nested list
print(matrix)
mixed_matrix = [["a", "b"],  # nested str
                [1, 2, 3],  # nested int
                [True]]  # nested bool

print(mixed_matrix)  # mixed nested list
print(type(mixed_matrix))
# -------------------------------------------------------
print("\nhow to access lists: indexing/slicing")
# access & read
lst = ["a", "b", "c", "d"]
# ------0-----1----2----3--- = indexing
print(lst)
print(lst[0])  # list first item
print(lst[-1])  # list's last item OR first item from the negative index
print(lst[-2])  # second last item from the negative index
print("access & read: nested list (matrix")
# we have to specify the row, the index and the column:
# matrix =  we get the whole list
# matrix [1] = if we want to access one row we call the number of the row
# matrix [1] [1] = we select a row and extract one value from it
matrix = [["a", "b", "c"],  # row 0
          ["d", "f", "e"],  # row 1
          [1, 2, 3]]  # row 2
print(f"whole list: {matrix}")  # whole list
print(f"first row {matrix[0]}")  # 1 specific row
print(f"last row {matrix[-1]}")  # last row
# specific value off specific row
print(f"first row first itme {matrix[0][0]}")
print(f"second row second item {matrix[1][1]}")
print(f"last row last item {matrix[-1][-1]}")
# -------------------------------------------------------
print("slicing")
# if we want to pick only sections of our list we can do the following:
# list[2:3] # would get from the second variable to the next
# but we can also pick no start list[:3] which will make us pick all variables from the begginning up to that point
# or no end: list[2:] which will pick all variables from that point onward in the list
# -----------4----3----2----1---negative index
lst = ["a", "b", "c", "d"]
# -----------0----1----2----3---positive index
print(lst[:2])
# from start to variable (first 2 chars in this example)
print(lst[2:])
# from variable to end (last 2 chars in this example)
print(lst[:])  # gets the whole list
print(lst)  # we simply write list if we want it all instead
print("Slicing matrix: ")
mat = [["a", "b", "c"],  # row 0
       ["d", "f", "e"],  # row 1
       [1, 2, 3]]  # row 2
print("slicing rows")
print(mat[:2])  # first two lists
print(mat[1:])  # last two lists
print("slicing within a matrix's row")
print(mat[2][:2])  # first [] is the row, second [] the slice
# -------row-slice of row
print(mat[0][1])  # first row, second value after start of the row
print(mat[1][1:3])  # second row, last 2 values
# -------------------------------------------------------------------------------------
print("\nUNPACKING: taking items out of the lists to put them into viariables ")
# we might want to take items out of lists to do the following:
# a name to calculate it's len
# a number or a date to confront it with another
# city name, or maybe a role, to filter or process it
# EXAMPLE:
person = ["Daniel", 20, "Data Analyst", "United kingdom"]
# ------------0------1--------2---------------3------
# name  = person[0] # extracting the name
# age = person[1] # age
# role = person[2] # role
# country = person[3] # country
# unfortunatly if we had alot of variables to unpack, this would become quite quickly too much to handle,
# for unpacking everything all together we can:
# the order of our variable names must match the list, be careful
# this makes everything cleaner and easier to read while also keeping it within 1 line
name, age, role, country = person
print(country, name)  # showing that it unpacked the variables from the list
# -------------------------------------------------------
# if there are some variables within a list we don't care much about,
print("\nREST COLLECTOR: asterisk *")
# we could rearrange those we don't care about together in the list and extract them together
# while unpacking one or more singular variables from the positive or negative index separately
# be careful though those we want packed together need to be near eachother
# also you can use only ONE * per unpacking
user = ["Dani", "#23544", "20-09-2026", "Spain", "costumer"]
# username, user_id, date, country, user_type = user / instead of writing this:
# we can use * to merge together the variables we want merged and might consider unnecessary
username, user_id, *details, user_type = user
# we could keep adding information to said list as we see fit and perhaps work with it later or not, as we see fit.
print(username)  # unpacks singularly
print(user_type)  # unpacks singularly
print(details)  # unpacks the rest
# ----------------------------------------
# maybe we care only about one variable, we can order them in a way that allows us to use the * to group the rest while unpacking the one we care about singularly like so:
user = ["Ella", 20, "Spain", "costumer", "20-09-2026"]
username, *details = user
print(username)
print(details)
# we can obvioyusl also do it from the opposite way:
costumer = ["Ella", 20, "costumer", "20-09-2026", "United Kingdom"]
*details, country = costumer
print(country)
print(details)
# example with only 1 value:
n = [1]
first, *details = n  # * collects the rest of the values and it's fine if there are none
print(first, details)
# -----------------
# other rules for unpacking:
# 1) the number of variables must match the number of values (unless we use * which could fix the issue)
# example: if we have n = {1,2,3} we must match all 3 values
# so first, second, third = n
# if we had one too many values/variables python would return a error.
# 2) unpacking can be used with: lists, str, tuples, etc
welcome = "hi"  # example with a str
hey, *other = welcome  # we extract only the first letter here leaving the resto to the *
print(hey, other)
# -------------------------------------
print("\nSKIPPING ITEMS: underscore _ ")
# if we want to skip items withing a list of variables we can use underscore (_)
print("skip the last item with _")
info = ["Rob", 23, "UK", "Bristol", "12-04-2013", "#345"]
name, *details, _ = info  # _ skipped the last value in the variable for us
print(name, details)
print("\n skip with both * and _")
info = ["Rob", 23, "UK", "Bristol", "12-04-2013", "#345"]
# unpacked name and nation, grouped city and date together and skipped the rest (age and id)
name, _, nation, *details, _ = info
print(name, nation, details)
print("\nskip everything in the middle with: *_")
info = ["Rob", 23, "UK", "Bristol", "12-04-2013", "#345"]
name, *_, id = info
print(name, id)
# IMPORTANT: *_ throws the variables away *variable instead stores them together separatly
# USE CASE: we unpack to make it easier for us to work with different pieces of a list, separatly
# ----------------------------------------------------------------
print("\n Explore and analyse: ")
print("\nANALISYNG using functions:")
# using functions to analyze our data:
# min() - max() - sum() - len() - all( - any())
lst = [3, 5, 7, 4, 3]
# ------0-1-2-3-4---index values
print("min:", min(lst))  # returns lowest value in the list
print("max:", max(lst))  # returns highest value in the list
print("sum:", sum(lst))  # returns sum of all values in the list
# sum won't work if you have a mix of different value types, requires ints/floats to work
print("length:", len(lst))  # returns number of characters in the list
# returns true because we have valid values for all items
print("all:", all(lst))
# returns False because it considers 0 as a missing value
print("all - 0 example:", all([1, 0, 3]))
# returns false because a empty string is considered a missing value
print("all - empty string example:", all(["a", "b", ""]))
print("any:", any(lst))  # true for aslong as one value returns True
print("any - 0 example:", any([1, 0, 3]))  # still returns true
print("any - empty string example:", any(["a", "b", ""]))  # even here
# 0 None and a empty string all return false, any has no true values so it returns False
print("any - no values example:", any([None, 0, ""]))
# -----------------------------------------------------------------------------
print("\nANALISYNG using methods: count, index")
# using count(a) and index(a) to search and count our data:
# count(a) is used to show us how many times a item appears in our list
# the number 3 appears twice in our list
print("count how many times 3 appears in our list:", lst.count(3))
# index(a) returns the position of the FIRST occurrance of a value (which is why the second 3 is not returned)
# index can also only retrieve positive numbers and not negative numbers.
# python counts values from 0 so it counts here 0,1,2,3  and it finds it
print("index of 4:", lst.index(3))
print("\nANALISYNG with operators: in, is, ==, <, >")
# in checks if a value is present in our sequence, returns boolean
# can be used with numbers, ints and str
print("in example:", 5 in lst)
print("in example:", 5 not in lst)  # false because it's in the sequence
print("in example:", 2 in lst)
# == compares, in this case lists to find if they are the same or not:
lst1 = [1, 2, 3]
lst2 = [5, 2, 3]
# they have different values
print("example of two different lists:", lst1 == lst2)
# in the case of > > comparison operators python compares the first element, if those are different it returns a boolean, if they are the same it checks the next and so on and forth:
lst1 = [5, 3, 3]
lst2 = [5, 2, 3]
# python checks the first value, both are 5 = equal, so it checks the second, finds that lst1 value isn't lower than lst2 and returns False
print("< operator with first value equal to the other which returns: ", lst1 < lst2)
# is operator checks the python ids of values rather than the values stored in the variables which is why 2 lists with identical values, on paper return False because they are stored in python with different ids:
lst1 = [5, 2, 3]
lst2 = [5, 2, 3]
print("is used on identical values but different memory stored ids: ", lst1 is lst2)
# it's like asking: are the two lists pointing to the same address? the answer is no
# ------------------------------------------------------------------------
print("\nADD-REMOVE-UPDATE LISTS:")
# .append() - insert() -
# .append("d") this is used to add to the end of a list a new item
lst = ["a", "c", "d"]
print(lst)
lst.append("f")  # appends to the end of the list the new variable
print(".append() to add at the end of a list: \n", lst)
# can append more than just 1 value, and it can be of different types
lst.append(1)
print("can keep using append: \n", lst)
# ------------------------------------------------------
# .insert(index, value) = .insert (1, b) used to add a item at the exact index of a list
lst.insert(1, "b")  # inserting as new index 1
print(lst)
lst.insert(4, "e")  # inserting as new index 4
print(".insert(position, value) ADD ITEMS: change the list: \n", lst)
# ---------------------------------------
mat = [["a", "b", "c"],
       ["d", "e", "f"],
       [1, 2, 3]]
mat.append([4, 5, 6])  # adding to the end of the matrix
mat.insert(0, ["a", "a", "a"])  # adding at index 0 of the matrix
print("ADD a row to the matrix: \n", mat)
# ---------------------------------------------------------------------
print("\nADDING A NEW VALUE TO A ROW IN A MATRIX")
mat = [["a", "b", "c"],
       ["d", "e", "f"],
       [1, 2, 3]]
mat.append(4)  # all this does is initiate a new row, not add to a existing one
print("initializing a new row in a matrix: \n", mat)
# ------------------------------------------------------
mat = [["a", "b", "c"],  # row 0
       ["d", "f", "g"],  # row 1
       [1, 3, 4]]  # row 2
mat[2].append(5)  # row 2 append at the end the new value (5 in this case)
mat[1].insert(0, 1)  # row 0 insert at index 0
print("\nadd a value to a existing row: \n", mat)
mat = [["a", "b", "c"],  # row 0
       ["d", "f", "g",],  # row 1
       [1, 3, 4]]  # row 2
mat[0].append("x")  # row 0 append at the end
mat[1].insert(1, "e")  # row 1 insert at index 1
print("add a value to a existing row 2: \n", mat)
# ---------------------------------------------
# remove old,bad data or duplicates
print("\n CHANGE your list: REMOVE ITEMS: ")
# .clear() remove everything and returns the list to a empty one
lst = ["a", "b", "c", "b"]
lst.clear()  # clear the whole list
print("clear used on a list returns a empty list: \n", lst)
# .remove("a") searches for the first match and removes it
lst = ["a", "b", "c", "b"]
lst.remove("b")  # removes the first instance of the value "b", not all of them
lst.remove("b")  # we can repeat the instruction if we want to
print("\nremove first selected value found: \n", lst)
# .pop() remove a item in a specific index and returns it to you
lst = [1, 2, 3, 4]
# ------0-1-2-- = indexes
lst.pop(1)  # removes the value at index 1
lst.pop()  # if you don't specify the value pop removes the last item
print("remove a item in a specific index: \n", lst)
print("\nREMOVE AND RETURN THE REMOVED ITEM:")
lst = [1, 2, 3, 4]
removed = lst.pop(3)  # removes and stores the removed item
print("remove a item: \n", lst)
print("removed item value: ", removed)
# ---------------------------------------------------------------
print("\nREMOVE rows FROM A MATRIX: ")
mat = [["hi", "a", "b"],  # row 0
       ["c", 1, "d"],  # row 1
       [1, 2, 4]]  # row 2
# removes a value in a list (in this case a entire row)
mat.remove(["c", 1, "d"])
mat.pop(0)  # oremoves a index in a list (in this case a entire row)
print("removed row with remove and pop: \n", mat)
# --------------------------------------------------
print("\nREMOVING A VALUE FROM A MATRIX")
# to remove a value in a matrix we need to first tell python to look into the child
# and then we can tell python to remove a value:
# in the list below: mat.remove("hi")
# wouldn't work we need to specify the row first
mat = [["hi", "a", "b"],  # row 0
       ["c", 1, "d"],  # row 1
       [1, 2, 4]]  # row 2
mat[0].remove("hi")  # removing by value from a row
mat[-1].pop(2)  # removing by indexed item from a row
print("remove a value/index using remove/pop 1: \n", mat)
mat = [["a", "b", "c"],  # row 0
       ["d", "f", "e"],  # row 1
       [1, 2, 3]]  # row 2
mat[-1].remove(3)  # removing by value from a row
mat[1].pop(0)  # removing by indexed item from a row
mat[0].pop()  # pop() left empty removes the last item
print("remove a value/index using remove/pop 2: \n", mat)
# ------------------------------------------------
print("\nCHANGE DATA: UPDATE ITEMS:\n")  # lst[2] = "e" for example
lst = ["x", "b", "x"]
lst[0] = "a"  # update the value at the given index with a new one using =
lst[-1] = "c"
print("updating a value using = : \n", lst)
print(type(lst))
# be careful what and how you update:
lst = ["a", "b", "c"]
lst = "x"  # not mentioning the value to change with lst[value]
# means we change the value of the whole list
print("convert a list into a str using =: \n", lst)
print(type(lst))
# we changed the value type of lst from list to type as we can see with this update
# --------------------------------------------
mat = [["a", "b", "c"],  # row 0
       ["d", "f", "e"],  # row 1
       [1, 2, 3]]  # row 2
mat[-1] = ["h", "i", "l"]  # updating a whole row
mat[0][0] = "-"  # updating ONE value
mat[1][1] = "-"  # updating ONE value
mat[-1][-1] = "-"  # updating ONE value
print("\nupdate a list's row and specific values in a matrix using =: \n", mat)
# --------------------------------------------------------------
print("\nORDERING LISTS; method: sort() - function: sorted() - reverse()")
# case scenarios: we want to sort items by most expensive to least
# list of costumers name we want organized alphabetically
# method: sort() - if it's str sort alpjabetically (ascending)
# if int, by highest to lowest
lst = ["b", "a", "c"]
lst.sort()  # if left empty it organizes it alphabetically
print("str ascending: ", lst)
lst = [3, 2, 1]
lst.sort()  # if left empty it organizes it alphabetically
print("int ascending: ", lst)
# --------------------------------------------------------
lst = ["b", "a", "c"]
lst.sort(reverse=True)  # reverse=True gives us the descending order
print("str descending: ", lst)
lst = [3, 2, 1]
lst.sort(reverse=True)  # reverse=True gives us the descending order
print("int descending: ", lst)
# -----------------------------------------------------------------
# str sorts based on ascending/descending order based on the first value in each list of a list like so:
print("\nORDERING LISTS WITHIN A MATRIX")
mat = [["b", "a", "c"],
       ["f", "d", "e"],
       ["b", "z", "g"]]
mat.sort()  # ascending order of lists containing str
print("str ascending: \n", mat)
mat = [["b", "a", "c"],
       ["f", "d", "e"],
       ["b", "z", "g"]]
mat.sort(reverse=True)  # reverse=True gives us the descending order
print("str descending: \n", mat)
mat = [[2, 3, 1],
       [7, 2, 5],
       [3, 5, 3]]
mat.sort()  # ascending order of lists containing int
print("int ascending: \n", mat)
# also sorting lists within lists is processed by python through comparing the first value in each list
# be aware that sorting doesn't work if in the list there's both instances of different data types, like str and int
# ---------------------------------------
print("\nORDERING VALUES WITHIN A SPECIFIC LIST IN A MATRIX")
# how to sort the values within only one specific list in a matrix
mat = [["b", "a", "c"],
       ["f", "d", "e"],
       ["b", "z", "g"]]
mat[1].sort()  # ascending order of specific list values
print("ascending order of values within a list in a matrix: \n", mat)
mat = [["b", "a", "c"],
       ["f", "d", "e"],
       ["b", "z", "g"]]
mat[0].sort(reverse=True)  # descending order of specific list values
print("descending order of values within a listin a matrix: \n", mat)
# -----------------------------------------------------------------
# function = sorted()
print("\nCREATING A SORTED COPY OF A LIST: funct = sorted(")
# lst = sorted(lst) ascending / lst = sorted(lst, reverse=True) descending
# here we pick a existing list we want sorted, we keep the original in it's current state and make a copy that's sorted the way we like it.
lst = ["b", "a", "c"]
# create a new variable that stores the new ascending list for us
lst_copy = sorted(lst)
# the original list is still intact and unchanged
print("original list: ", lst)
print("copied ascending list: ", lst_copy)  # while the new is organized

lst = ["b", "a", "c"]
lst_copy = sorted(lst, reverse=True)  # descending new list
print("copied descending list: ", lst_copy)
# -----------------------------------------
print("\nSORTED COPY OF A MATRIX LIST: funct = sorted()")
mat = [["b", "a", "c"],
       ["f", "d", "e"],
       ["b", "z", "g"]]
# ascending copy "reference" order of list within a matrix
mat_copy = sorted(mat)
print("original matrix: \n", mat)
print("ascending ordered copy of list within matrix: \n", mat_copy)
# ----------------------------------------
print("\nREVERSING LISTS: method = .reverse() function = reversed()")
# fully reversing the list, first becomes last, last first and so on
lst = ["a", "b", "c", "d"]
lst.reverse()  # reverses completely the list order
print("reversed list: ", lst)
# ---------------------------------------------------------
# we can also create a copy "reference" and reverse it with the function
# reversed(lst)
lst = ["a", "b", "c", "d"]
lst_copy = reversed(lst)  # reversed copy "reference" of a list
print("reversed iterator copy: ", lst_copy)
# reversed doesn't create a reversed copy of the list but rather a iterator object of the list look for more info about it in the advanced topics session.
# we can convert this iterator outcome for now into a list using the function list()
# converts the iterator lst using the function list()
lst_copy = list(reversed(lst))
print("list() used to convert the iterator copy into a flipped around list: ", lst_copy)
# ----------------------------------------------------
print("\nCOPY PYTHON LISTS SAFELY: assignment, shallow copy, deepcopy")
print("\nREFERENCE COPY: assignment = ")
# = is used to make a reference
# for example copy_lst = lst
# example:
lst = ["a", "b", "c"]
lst_copy = lst
# both variables lst/lst_copy reference the same list in the memory which means:
lst.pop()  # the same variable will be removed from both
lst_copy.append("z")  # the same variable will be added to both
print("original:", lst)
print("assignment copy (reference): \n", lst_copy)
# this is to say that changing a copy reference can be risky because it can affect other variables aswell.
# --------------------------------------------------
print("\nCOPYING LIST: SHALLOW COPY: method: .copy()")
# what if we want a copy so that the copy's the only one affected by changes?
# we can use the method .copy()
lst = ["a", "b", "c"]
lst_copy = lst.copy()  # not a reference a actual copy
lst.pop()  # so this affects only lst
lst_copy.append("z")  # and this affects only the copy
print("original:", lst)
print("shallow copy:", lst_copy)
# way safer method than doing just an assignment
# ------------------------------------------
print("what happens when we try to modify a matrix?")
# unfortunatly the .copy() only allows to change at a "shallow level" (first level)
# what that means is that even if we are able to, as the example below, change the first level of the matrix, aka the rows, it's "children" (deeper level) are still pointing to the same original variables
mat = [["a", "b",],  # row 0
       ["c", "d",]]  # row 1
mat_copy = mat.copy()
mat.pop()  # this targets the rows which are at a shallow level ( first level) so we can modify this using .copy()
# but this affects the row's children at a deeper level, which both the original and the copy() share, so they both get modified
mat_copy[0].append("z")
print("original: \n", mat)
print("shallow copy: \n", mat_copy)
# ---------------------------------------------------------
print("\nDEEP COPY: copy module functions  = copy - deepcopy")
# mat_copy = copy.copy(mat) works exactly like the intbuilt shallow copy but it's not limited to only lists
# mat_copy = copy.deepcopy(mat) module function instead works differently:
mat = [["a", "b",],  # row 0
       ["c", "d",]]  # row 1
# deepcopy function imported from the import copy module
mat_copy = copy.deepcopy(mat)
mat.pop()
# thanks to the module here we are able to only append to the first row the wanted value
mat_copy[0].append("z")
print("original: \n", mat)
print("deepcopy: \n", mat_copy)
# --------------------------------------------------------------
print("\nis operator used to compare lists:")
mat = [["a", "b",],  # row 0
       ["c", "d",]]  # row 1
print("\nASSIGNMENT")
mat_copy = mat  # assignment
# returns True because mat_copy is just a reference and uses the same memory stored values
print("reference copy = original ", mat is mat_copy)
print("\nshallow copy")
mat_copy = mat.copy()  # copy method
# a shallow copy has a different first level stored, making mat and mat_copy different
print("copy method = original? ", mat is mat_copy)
# true a shallow copy affects only the first level, so the row values are shared and stored in memory as the same
print("copy method row = original row?", mat[0] is mat_copy[0])
print("\ndeepcopy")
mat_copy = copy.deepcopy(mat)  # deepcopy module function
# memory stored completely differently at any level
print("deepcopy = original?", mat is mat_copy)
# memory stored completely differently at any level
print("deepcopy = original?", mat[0] is mat_copy[0])
# so to recap, use the is operator to understand whether values are indipendent or not
# --------------------------------------------------
print("\nrecap about copy methods:")
# assignment, isn't safe try to avoid it
# copy method, shallow copy is good and safe for aslong as there isn't nesting
# import method deepcopy allows us to work with nesting and matrixes but makes our code heavier since we need to download a library for it
# copying is useful for experimenting and testing, avoid it otherwise
# -------------------------------------------------------------------------------------
print("\nCOMBINING DATA")
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
comb = letters + numbers  # sum operator to combine lists
# the order of the item is determined by how we compile them, the letters appear first in the list because we write:
# comb = letters + numbers instead of comb = numbers + letters
print("list sum: ", comb)  # compiling with +
print("list sum: \n", letters + numbers)  # alternative way to compile using +
print("list multiplication: \n", letters * 2)

print("\nWhat if we want to keep the lists separate?")
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
comb = [numbers, letters]  # making a nested list, two isolated rows
# comb = [letters] + [numbers] - or sum them like this
# comb = [letters] * 2 - or multiply them like this
print("sum: ", comb)
# -------------------------------------------------------------
print("\nEXTEND: .extend()")
# doesn't create a new list, extends a existing one
# this allows us to avoid having to create a new list, although we can do the same within the print as we've seen.
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
letters.extend(numbers)  # modifies and adds like append
# extend(numbers) estends the letters to add what's in pharentesis kind of works like .append()
print("extension of letters: ", letters)
print("untouched numbers: ", numbers)
# -----------------------------------------------
print("\nCOMBINING USING the function: zip(): ")
# allows us to pair variables within lists
# if zip is used to pair variables from two lists but one list is shorter than the other
# python is gonna stop at the shorter list
# the outcome of zip() are tuples although python returns it as a iterator, which if we want to use on the spot we'll have to convert to a list using list()
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]
comb = zip(letters, numbers)  # converting to iterable + pairing
print("pairing outcome = iterable by default: \n", comb)  # iterator outcome
letters = ["a", "b", "c"]
# 4 gets left out because python stops at the shortest variables list, so it stops after pairing c and 3 together
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers))  # converting using list
print("iterator converted using list(): \n", comb)
# alternativly we can write the list() within the print rather than in the comb value declaration
print("list() used in the print: \n", list(comb))
print("\npairing with a str")  # a str is a sequence so what happens is the values within it get treated exactly like a list, so in the example below the final 0, just like the 4 get neglected because python writes only up to the shorted of the lists aka letters which has 3 variables
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers, "hello"))
print("adding and pairing a str: \n", comb)
# ----------------------------------
# EXAMPLE: build the relationship between the values below
id = [1, 2, 3]
names = ["Dan", "Rob", "Bob"]
age = [21, 5, 63]
print("user data: \n", list(zip(id, names, age)))
# -------------------------------------------------------------
print("ITERATOR VS ITERABLE: enumerate, map, filter")
print("\nITERATING THROUGH OUR DATA:")
# if we store alot of data, lists, dict, int, float, bool, str etc, we risk filling up our memory alot, to make this less of a problem we can select the data we want to work on using:
# ITERATORS: zip(), enumerate(), chain(), map(), reversed()
# these produce objects one by one as long as we are asking for them, making the memory load much easier to manage.
# we need iterators to: 1) loop items 2) save memory 3) speed flexibility (data pipelines)
# ITERABLE: the thing that we can loop over, a container, a sequence of items we can use iterate over using iterators.
# example:
letters = ["a", "b", "c"]
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)
# letters is the iterable we create a loop we do some iterations then maybe we store it into another list and loop through it all.
# -----------------------------
print("\nENUMERATE: enumerate(iterable)")
# built in function - iterator object
# as it iterates through a list, it gives us both the values and the indexes of said values.
# we can either do enumerate(iterable)
# or if we want to chose the starting index enumerate(iterable start = 1) for example
letters = ["a", "b", "c"]
# the output is a iterator with a iterator type and a memory address
print("iterator type + memory address:\n", enumerate(letters))
# if we want to be able to see the content of this iterator we can convert it to a list()
print("converted iterator + index:\n", list(enumerate(letters)))
# and maybe we want to start from a different index:
print("converted iterator + index:\n", list(enumerate(letters, start=1)))
# -----------------------------
# we use this iterator to build a for loop generally:
letters = ["a", "b", "c"]
for index, value in enumerate(letters, start=1):
    print(index, value)
print("index and value in our list\n")
# index is the memory stored index of a value, value represents the values within letters
# -------------------------------------------------------------------
# USE CASE: find the exact position of bad stored data
# EXERCISE:
letters = ["a", "", "c"]
for index, value in enumerate(letters, start=1):
    print(index, value)
print("looping to find bad data in our list\n")
# --------------------------------------------------------------------
print("\nREVERSED: reversed()")
letters = ["a", "b", "c"]
# returns iterator + memory so we convert it using list
print("iterator type + memory address:\n", reversed(letters))
print("converted iterator into reversed list:\n", list(reversed(letters)))
for l in reversed(letters):
    print(l, end=" ")  # of course we can loop over it once again
# -----------------------------------------
# function used in order to combine lists into pairs (tuples)
print("\nZIP ITERATOR")
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
# returns iterator + memory so we convert it using list
print("iterator type + memory address:\n", zip(letters, numbers))
print("iterator type + memory address:\n", list(zip(letters, numbers)))
# once again lets iterate some iterables in different lists through a loop
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
for l, n in zip(letters, numbers):
    print(l, n)
print("\ncombining lists and giving us back iterables")
# combining two lists and giving back iterables we can work with
# ---------------------------------------------
print("\nMAP ITERATOR: map(function, iterator)")
# fast and clean way to transform data
letters = ["a", "b", "c"]
# returns iterator + memory so we convert it using list
# use the upper method that we find within this class (str in this case)
print("iterator type + memory address\n", map(str.upper, letters))
print("upper applied to a list:\n", list(map(str.upper, letters)))
# -----------------------
# other example: we want to change this sequence of str into one of int
numbers = ["1", "2", "3"]
print("converted list into integers\n", list(map(int, numbers)))
# in this case we didn't even use a function, we just specified the class type
# ---------------------------
# other example:
names = [" Luca ", "John ", " Ann"]
print("clean names off bad data\n", list(map(str.strip, names)))
# --------------------------
# used in a for loop
names = [" luca ", "john ", " ann"]
for n in map(str.strip, names):
    print(n)
print("looping to clean bad data:")
# --------------------
print("\nFILTER ITERATOR: filter(function, iterable")
# filtering data, for example maybe we want only numbers, or certain names etc
# clean up the list by removing invalid/bad data:
letters = ["a", "", "b", None, "c", False]
# with None, or bool we filter out any falsy data, so it affects None, a boolean and the empty space in this case
print("filtering bad data with filter(None,iterable)\n",
      list(filter(None, letters)))
# example with bool
letters = ["a", "", "b", None, "c", False]
print("filtering bad data with filter(None,iterable)\n",
      list(filter(bool, letters)))
# ------------------------
items = ["sql", "123", "html", "44"]
print("\nstr.isalpha to remove any non str data:\n",
      list(filter(str.isalpha, items)))
print("str.numeric to remove any non int data:\n",
      list(filter(str.isnumeric, items)))
print("example in a loop")
for i in filter(str.isalpha, items):
    print(i)
# ----------------------------
