print("FORMATTED STRINGS:")
# used to format together strings, we call the string value of first and second using curly braces enveloping these then, we use the " " to create a space and we use + signs to formate them together
first = "Daniel"
last = "Emmingham"
full = first + " " + last
print(full)
# while this is not wrong there is another, simpler method to do this, here we start with f to call a string formatting, use curly braces to envelop the strings and we leave a space bethween them to generate the space
first = "Daniel"
last = "Emmingham"
full = f"{first} {last}"
print(full)
# we can also inbuild the len function to call in the length of a string such as like this:
first = "Daniel"
last = "Emmingham"
full = f"{len(first)} {last}"
print(full)
# here's another example, adding moltiplications
first = "Daniel"
last = "Emmingham"
full = f"{len(first)} {2 + 2}"
print(full)
