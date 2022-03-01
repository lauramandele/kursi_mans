years = float(input("For how long do you work here?"))
bonus_years = years - 2
if (bonus_years >= 0):
    salary = float(input("What is your monthly salary?"))
    print(f"Your bonus will be {round(salary*0.15, 2)}")
else:
    print("Sorry, your bonus is 0")




