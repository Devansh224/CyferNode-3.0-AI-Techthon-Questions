# Your code here

def decrypt(line):
    res = []
    for i in line:
        if 'A' <= i <= 'Z':
            res.append(chr((ord(i)-ord('A') + 13)%26 + ord('A')))
        else:
            res.append(i)
    return ''.join(res)


with open('secrets.txt', 'r') as file:
    line = file.read()
# print(line)
print(decrypt(line))