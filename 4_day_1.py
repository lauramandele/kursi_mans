start_num = 1
end_num = 100
end = ","
for i in range(start_num, end_num+1):
    value = ""
    if i % (5 * 7) == 0:
        value += "FizzBuzz"
    elif i % 5 == 0:
        value += "Fizz"
    elif i % 7 == 0:
        value += "Buzz"
    else:
        value += str(i)
    if i == end_num:
        end = "\n"
    print(value, end = end)

