def main():
    print("Hello World")
    print("\n")

if __name__ == '__main__':
    main()

#Exercise 1
# Find all the factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10 % 3 = 1
x = 52633
print("Excercise 1: Factors of", x)
for i in range(2, x):
    # your code here
    if x % i == 0:
        print(i)
print("\n")

#Exercise 2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    print(f"Excercise 2: Factors of {x}")
    for i in range(2, x):
        if x % i == 0:
            print(i)

print_factor(52633)
print("\n")

#Exercise 3
# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
print("Excercise 3: Factors of numbers in the list")
# your code here
for number in l:
    print(f"Factors of {number}:")
    for i in range(2, number):
        if number % i == 0:
            print(i)
    print("\n")