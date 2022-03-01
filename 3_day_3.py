a = float(input("Enter a number"))
b = float(input("Enter an other number"))
c = float(input("Enter one more number"))

upper = a
middle = b
lower = c

if a > b:
    if b < c:
        lower = b
        middle = c
        if a < c:
            upper = c
            middle = a
else:
    middle = a
    upper = b
    if a < c:
        lower = a
        middle = c
        if c > b:
            upper = c
            middle = b

print(lower, middle, upper,',')