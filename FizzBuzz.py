count = 0

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        count += 1

    elif i % 3 == 0:
        print("Fizz")
        count += 1
    
    elif i % 5 == 0:
        print("Buzz")
        count += 1

    else:
        print(i)
        count += 1

print(f"The number of comparisons done is:", count)
