# print 7-times table
# from 1 to 10 using a for loop
# must look exactly like:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

total = 0
for number in range(7, 71, 7):
    total += 1
    print(f"7 x {total} = {number}")
# can also be written as such:
for number in range(1, 11):
    print(f"7 x {number} = {7*number}")
# and like this
for number in range(1, 11):
    total = 7*number
    print(f"7 x {number} = {total}")
# ------------------------------------------------------------
