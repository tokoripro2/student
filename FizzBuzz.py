
for i in range(101):
    number = int(i)
    if (number % 3) == 0 and (number % 5) == 0:
        print("Fizz Buzz")
    elif (number % 3) == 0:
        print("Fizz")
    elif (number % 5) == 0:
        print("Buzz")
    else:
        print(str(number))