import math
n = int(input())
dict = {}
for j in range(n):
    l1 = [int(i) for i in input().split()]
    c = (math.sqrt((l1[0]**2) + (l1[1]**2)) / l1[2])
    if c in dict:
        dict[c] += 1
    else:
        dict[c] = 1
sum = 0
for d, count in dict.items():
    sum += int((count*(count-1))/2)
print(sum)


# 5
# 5 12 1
# 16 63 5
# -10 24 2
# 7 24 2
# -24 7 2
