res = []
with open("nginx_logs.txt", 'r', encoding='utf8') as f:
    for line in f:
        ln = line.split()
        res.append((ln[0], ln[5].split('"'), ln[6]))
print(res)
