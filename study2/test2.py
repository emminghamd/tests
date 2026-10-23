
# given a list of numbers and print numbers that satisfy these conditions:
# 1) the number must be divisible by 3
# 2) if the number is greater than 100 skip it
# 3) if the number is greater than 150 stop the loop

items = [132, 9, 54, 170, 99, 120, 12, 76, 30]
while item in items / 3:
    if item >= 100 and item < 150:
        continue
    if item >= 150:
        break
    else:
        print(f"the selected numbers are: {item}")
