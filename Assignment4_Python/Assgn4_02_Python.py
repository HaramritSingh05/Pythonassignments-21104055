#QUESTION 2
'''Python program to print the Pascal’s triangle for n number of rows
given by the user using both recursive and iterative procedures'''

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle\n'))

print("USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")
