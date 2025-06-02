# Finger Exercise Lecture 6
# Assume you are given an integer 0 \<= N \\<= 1000.
# Write a piece of Python code that uses bisection search to guess N. 
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. 
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = int(input("Enter your N (0-1000): "))

count = 0
low = 0
high = 1000
guess = (high + low)//2

while guess != N:
    if guess > N:
        high = guess - 1
    else:
        low = guess + 1
    guess = (high + low)//2
    print(f"Guess: {guess}")
    count += 1
        
if guess is not None:
    print(f"N: {guess:.4f}")
    print(f"Steps in bisection search: {count}")