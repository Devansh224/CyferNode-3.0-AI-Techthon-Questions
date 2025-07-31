'''

You are provided with two variables having a string each from the mystery.txt file,
your job is to find the intersection of those two values and print it to get the password to the Excel file.
Make sure the final answer is arranged in alphabetical order!

Good Luck Codebreakers!
'''

def intersection(str_1, str_2):
    # Your code here
    return None



with open('mystery.txt', 'r') as file:
    lines = file.readlines()

str_1 = lines[0].strip()
str_2 = lines[1]
print(intersection(str_1, str_2))
