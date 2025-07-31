'''

You are given a string from the mystery.txt file, 
find the duplicates in the string and reverse it to get the password for the Excel file.
Make sure the final answer is arranged in alphabetical order!

Good Luck Codebreakers!

'''

def duplicate(line):
    # Your code here
    dup = set()
    free_ah = []
    for i in line:
        if i not in dup:
            dup.add(i)
            free_ah.append(i)
    return ''.join(sorted(free_ah[::-1]))


with open('mystery.txt', 'r') as file:
    line = file.read()

print(duplicate(line))