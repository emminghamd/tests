# TYPE CONVERSION
x = input("x: ")
# type is a inbuilt function that passes an object as an argument and returns it's type
print(type(x))
# because at the moment x is a string, we have to convert x into a integer as follows:
y = int(x) + 1
# now we need to convert both x and y to formatted strings using f
print(f"x: {x}, y: {y}")
# x: is the label {x} is us formatting it, same goes for y
# y = x + 1
# we need to convert x to the same string type, to do so we can use the following
# int(x) used for integers
# float(x) used for floats
# bool(x) used for booleans
# str(x) for strings
