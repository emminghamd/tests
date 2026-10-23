print("Data Structures: list, tuple, set, dictionaries")
# all data structures have 4 characteristics: 
# ORDERED - DUPLICATES - INDEXES - MUTABLE
# lets check them applied to the list
print("\nLIST:") # list[1,2] - in a list everything is allowed
print("\nORDERED:") # python remembers the exact order of every variable in lists
my_list = [10,30,20,40,10] # index 0 - 1 - 2 - 4
print("python remembers the order of a list",my_list) 
print("\nDUPLICATES:")
print("python allows duplicates:",my_list)
print("\nINDEXES:")
print("we can access variables through their index:",my_list[1])
print("\nMUTABLE:")
print("original list:",my_list)
my_list[0] = 40 # updating
print("updating",my_list)
my_list.append(50) # adding (at the end=)
print("addind at the end",my_list)
my_list.insert(1,60) # adding on a index
print("inserting at a index",my_list)
my_list.remove(20) # removing by value
print("removing",my_list)
my_list.pop(-1) # removing using the index
print("removing by index",my_list)
my_list.sort() # sorting the list
print("sorting",my_list)
my_list.sort(reverse=True) # reverse sorting the list
print("reverse sorting",my_list)
#-----------------------------------------
print("\nTUPLE:") # tuple (,1,2) - ordered list that cannot change after it's creation
# use case: we use tuples when we want to guarantee that no code can mutate our data, rendering it immutable and safe from changes
tuple_list = (10,30,20,10)
print("tuples are ordered, allow duplicates:",tuple_list)
print("tuples variables can be accessed by their index:",tuple_list[1])
print("the only possible mutation is sorted:", sorted(tuple_list))
# sorted works but functions won't work to mutate a tuple
# so a tuple has these characteristics: ORDERED - DUPLICATES - INDEXES
#-----------------------------------------
print("\nSET:") # set {1,2} - unique
# a set is a unordered collection of unique values
my_set = {10,30,20,10}
print("a set is unordered and doesn't allow duplicates: ",my_set)
# set variables aren't stored by a index but rather by a hash index
# making their order different but with the benefit of using the hash index which is faster to process fo python
# as we can see it also doesn't allow duplicates, as 10 duplicate gets removed by python
# print("a set is unordered and doesn't allow duplicates: ",my_set[1])
# calling for a index also wouldn't work, the print above would return a error
# because the values of a set aren't saved with a index, but with a hash index.
print("original list:",my_set)
my_set.remove(20) # removing by value
print("removing",my_set)
# sets are mutable but: won't allow:
# updating, append, insert, pop (because it doesn't have a index), sorting (because it's unordered), 
#---------------------------------------------------
print("\nsets methods:")
a = {10,20,30,40}
a.add(50) # the new variable must be unique
# and will be ordered based on the hash index
print("add = add a new unique variable (hash index ordered:)", a)
a.add(10) # 10 already exists so python just ignores it
print("example of trying to add a pre-existing unique value:)", a)
#--------------------------------------
# .update() - merges another group o variables (iterables) into the set
a.update("hi") # adds the new list to the set
print(".update() = merge a list to a set:", a)
a.update((1,2))
print(".update to add a list to the set:", a)
a.update({1,2})
print("update to add a set to the set:", a)
# we can also use math operators as shortcuts:
# |= instead of update BUT IT WORKS ONLY FOR SET IN A SET
a |= ({1,2})
print("update to add a set to the set (only works if we merge the same type of data structures):", a)
#-----------------------------------------
# .remove() be careful, returns an error if the value is missing
b = {10,20,30,40}
# a.remove(100) because the value is missing from the set this would return a error
b.remove(10)
print(".remove(10) to remove said value:", b)
#------------------------------------------------
# we have a safier way to remove items, so that we don't risk getting back errors:
# .discard
c = {10,20,30,40}
c.discard(10) # removing the value
c.discard(100) # value doesn't exist but no error gets returned, this method just gets ignored by python
print(".discard() safier method to remove a value:",c)
# a.pop() also works, but it removes a random variable since the index of values and the hash index don't coincide
#-----------------------------------------
print("\nSET: math methods:")
# 

a = {10,20,30,40}
b = {30,40,50,60}
print(".union() combine unique values from multiple sets:",a.union(b)) 
# using | shortcut for .union()
print("shortcut",a | b)
# .union() combines all unique values from multiple sets
# union does not change the original sets however it just merges them together into a new set
print("original set a remains unchanged",a)
print("original set b remains unchanged",b)
# .intersection() shows shared variables
print("\n.intersection() to show shared values:", a.intersection(b))
# shortcut for .intersection() = &
print("shortcut",a & b)
# .difference() show values that are exclusive to only one set excluding those that overlap with the other
print(".difference() show exclusive values of one set", a.difference(b))
print("shortcut for the other set:", b - a) # shortcut for difference -
# symmetric._ifference() variables that are not overlapping at all between sets
print(".symmetric_difference() shows variables that are unique to both sets:", a.symmetric_difference(b))
#-------------------------------
print("\nRELATIONSHIP METHODS FOR SETS:")
# .issubset() # returns bool True if all items from 1 set exist in another
a = {10,20,30,40}
b = {30,40,50,60}
print(".issubset() False since items from 1 set exist in another:\n",a.issubset(b)) 
a = {30,40}
b = {30,40,50,60}
print(".issubset() True since items from 1 set exist in another:\n",a.issubset(b))
# .issuperset # bool True if one set has all the values from another 
print(".issuperset() True since the b set contains all values from a:\n",b.issuperset(a))
# case scenarios: we have a big table and we need to make sure that no costumer is in this table without having a id in said table
# and we have another table that holds for example the ids for VIP or for moderators/admins and the likes
# so we use a .issubset for the VIP table and the issuperset to check if said custumers are present in the master table.
#-----------------------------
# .isdisjoint() returns bool True if if both sets share no items
print(".isdisjoint() returns True if both sets share no common values:\n",a.isdisjoint(b)) # returns false since they share the values 30 and 40
# case scenario: used when we have one big data set and we want to split it in two without any overlapping data
#----------------------------------------
print("\nDICTIONARIES:") # dict {"a":1,"b":2} - used for mapping
