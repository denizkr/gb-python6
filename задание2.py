from collections import Counter
from urllib import request as req

with req.urlopen('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/'
                 'nginx_logs/nginx_logs') as file:
    base = [line.split()[0] for line in file]

ip, count = Counter(base).most_common(1)[0]
print(f'IP Адресс спамера: {ip.decode("utf-8")}, количество запросов: {count}')
