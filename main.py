from extras.desc import desc
from swap import swap

print("Please enter two numbers to swap to string:")
num1 = int(input())
num2 = int(input())
print(swap(num1,num2))

print("Please enter a number to print it in natural descending order:")
n = int(input())
desc(n)
