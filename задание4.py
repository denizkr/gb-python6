import sys

with open('users.csv', 'r', encoding='utf-8') as file1, \
        open('hobby.csv', 'r', encoding='utf-8') as file2, \
        open('users_hobby.txt', 'w', encoding='utf-8') as file3:
    for line1 in file1:
        line2 = file2.readline().strip()
        if not line2:
            line2 = None
        file3.write(f'{line1.strip()}: {line2}\n')
    content = file2.readline()
    if content:
        sys.exit(1)
