# Finger Exercise Lecture 5
# Assume you are given a string variable named my_str. 
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. 
# For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = "abcdefg"
new_str= ''
for i in range(len(my_str)):
    if i % 2 == 0:
        new_str += my_str[i]

print(new_str)