import datetime

# Exercise Age 100
username = input("Hello! Please enter your username:")
age = input(f"{username}, how old are you?")
age = int(age)
print(f"Omg, you will be 100 in {100-age} years")
year_now = datetime.datetime.now().year
print(f"It's going to be in year {year_now+(100-age)}")

# Exercise Room volume
print("Let's calculate room volume! ")
width = input("Enter width:")
length = input("Enter length:")
height = input("Enter height:")
volume = float(width) * float(length) * float(height)
print(f"Room volume is {volume}")

# Exercise Temperature Conversion
print("Temperature")
temp_celsius = input("Enter temperature in Celsius:")
temp_fahrenheit = 32 + (float(temp_celsius) * (9 / 5))
print(f"The temperature in fahrenheit is {round(temp_fahrenheit, 2)}")