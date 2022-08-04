# 가장 많이 등장하는 알파벳만을 사전 순으로 출력
import collections

my_str = input().strip()
result = collections.Counter(my_str)  # dict
arr = sorted([item[0] for item in result.items() if item[1] == max(result.values())])
print("".join(arr))
