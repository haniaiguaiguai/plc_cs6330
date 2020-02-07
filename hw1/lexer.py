import sys

filename = 'test.txt'
if len(sys.argv) > 1:
    filename = sys.argv[1]

tokens = []
with open(filename, 'r') as file:
    for line in file.readlines():
        char_list = []
        for c in line:
            if c.isalnum():
                char_list.append(c)
            else:
                if char_list:
                    tokens.append(''.join(char_list))
                    char_list = []
                if c != ' ' and c != '\n':
                    tokens.append(c)

for token in tokens:
    print(token)
