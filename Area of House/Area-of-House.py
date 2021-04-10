# This function multiplies two numbers.
def multiply(x, y):
    return x * y

# Program to find the area of a house.
print("This is a calculator to find the area of your house.")
print("Please enter all values in metres.")

# Ask user the length and breadth of living room.
a = int(input("Enter length of drawing room: "))
b = int(input("Enter breadth of drawing room: "))
lr=a*b
print(f"The area of your drawing room is {lr} sq. m.")

# Ask user the length and breadth of kitchen.
c = int(input("Enter length of kitchen: "))
d = int(input("Enter breadth of kitchen: "))
ki=c*d
print(f"The area of your kitchen is {ki} sq. m.")

# Ask user the length and breadth of bedroom 1.
e = int(input("Enter length of first bedroom: "))
f = int(input("Enter breadth of first bedroom: "))
br1=e*f
print(f"The area of your first bedroom is {br1} sq. m.")

# Ask user the length and breadth of bedroom 2.
g = int(input("Enter length of second bedroom: "))
h = int(input("Enter breadth of second bedroom: "))
br2=g*h
print(f"The area of your second bedroom is {br2} sq. m.")

# Ask user the length and breadth of bedroom 3.
i = int(input("Enter length of third bedroom: "))
j = int(input("Enter breadth of third bedroom: "))
br3=i*j
print(f"The area of your third bedroom is {br3} sq. m.")

# Ask user the length and breadth of bedroom 4.
k = int(input("Enter length of fourth bedroom: "))
l = int(input("Enter breadth of fourth bedroom: "))
br4=k*l
print(f"The area of your fourth bedroom is {br4} sq. m.")

# Ask user the length and breadth of bedroom 5.
m = int(input("Enter length of fifth bedroom: "))
n = int(input("Enter breadth of fifth bedroom: "))
br5=m*n
print(f"The area of your fifth bedroom is {br5} sq. m.")

# Add all the values to get area of house.
print(f"The total area of your house is {lr+ki+br1+br2+br3+br4+br5} sq. m.")
