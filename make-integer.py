import re
f = open('./result.txt', 'r')
fs = f.read().split('\n')[-1] # 마지막줄만 참조
f.close()
result = re.compile('[0-9]+')
result = list(map(int, result.findall(fs)))
print(result[1:])