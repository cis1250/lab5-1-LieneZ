#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def positive():
    num = -1
    while num < 0:
        try:
            num = int(input("How many Fibonacci terms do you want? "))
            if num < 0:
                print("Invalid input: please enter a positive integer.")
            else:
                continue
        except ValueError:
            print("Invalid input: please enter a positive integer.")

    return num

def fibonacci_seq(number):
    number = int(number)
    term2 = 1
    output = 1

    for i in range(0, int(number)):
        if i == 0:
            output = 0
        elif i == 1 or i == 2:
            output = 1
        else:
            term1 = term2
            term2 = output

            output = term1 + term2
        print_fib(output)

def print_fib(out):
    print(out, end=' ')


def main():
    fibonacci_seq(positive())

if __name__ == "__main__":
        main()

