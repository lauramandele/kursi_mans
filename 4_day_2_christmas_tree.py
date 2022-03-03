h = input("Enter the trees height:")
try:
    # Convert it into integer
    h = int(h)
    for i in range(1, h + 1):
        white = h - i
        stars = i * 2 - 1
        print(" " * white + "*" * stars)
except ValueError:
    print("Nooo... input is not a number")
