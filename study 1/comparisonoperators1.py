print("COMPARISON OPERATORS")
# used to compare values
print(" integer/float comparisons")
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 <= 20)
print(10.1 == 10.1)
print(10 == "10")
# here we get False because "10" is stored as a string type
print(10 != "10")
# != not equal operator which, returns True because 10 is a integer and "10" a string

print("string comparisons")
print("bag" > "apple")
# because bag comes "after" it's considered greater
print("bag" == "BAG")
# every letter has a numerical referentiation in programming b and B have different numerical referentiations which is why the boolean outcome is False
# we can use orb to demonstrate this as follows
print(ord("b"))
print(ord("B"))
