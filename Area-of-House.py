print('Enter all values in metres.')

a=float(input('Enter length of hall: '))
b=float(input('Enter breadth of hall: '))
print(f'Area of your hall is {a*b} sq. m.')

c=float(input('Enter length of kitchen: '))
d=float(input('Enter breadth of kitchen: '))
print(f'Area of your kitchen is {c*d} sq. m.')

no_of_bedrooms,bedroom_sum=int(input('Enter number of bedrooms: ')),0
for i in range(no_of_bedrooms):
    e=float(input(f'Enter length of bedroom {i+1}: '))
    f=float(input(f'Enter breadth of bedroom {i+1}: '))
    bedroom_sum+=e*f
    print(f'Area of bedroom {i+1} is {e*f} sq. m.')

print(f'The total area of your house is {(a*b)+(c*d)+bedroom_sum} sq. m.')