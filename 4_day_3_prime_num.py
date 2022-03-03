num = input("Enter a positive number ")
prime = True
try:
    # Convert it into integer
    num = int(num)
    if (num > 0):
        for i in range (2, num):
            if num % i == 0:
                prime = False
                print(f"{num} divides with {i}, so it's not a prime")
            break
        if prime:
            print(f"{num} is a prime number")

    else:
        print("It's not a positive number")
except ValueError:
    print("Nooo... input is not an integer number")
