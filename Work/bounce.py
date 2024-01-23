# bounce.py
#
# Exercise 1.5

day = 1
height = 100

while day <= 10:
    height = height * 3/5
    print(day, round(height, ndigits=4))
    day = day + 1