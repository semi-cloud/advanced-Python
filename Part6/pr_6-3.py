# 가장 많이 등장하는 알파벳만을 사전 순으로 출력
from collections import defaultdict

my_str = input().strip()
d = defaultdict(int)
for char in my_str:
    if char != "'":
        d[char] += 1
result = sorted([item[0] for item in d.items() if item[1] == max(d.values())])
print("".join(result))
