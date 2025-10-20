lolim, uplim = int(input("Enter lower limit: ")), int(input("Enter upper limit: "))
for i in range(lolim, uplim + 1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
