# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30

def add_mult (a, b, c):
    num_list = [a, b, c]
    print(f"My list: {num_list}")
    num_list.sort()
    print(f"After sorting: {num_list}")
    print(f"({num_list[0]}+ {num_list[1]}) * {num_list[2]}")
    return (num_list[0] + num_list[1]) * num_list[2]


result = add_mult(20, 5, 3)
print (f"result is: {result}")