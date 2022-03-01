your_temp = float(input("What is your temperature?"))
if(your_temp < 35):
    print("Not too cold?")
elif(your_temp >= 35 and your_temp <= 37):
    print("All right")
else:
    print("Possible fever")