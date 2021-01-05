import math
def mostActive(customers):
    arr = []
    n = len(customers)
    p = math.ceil(n * 0.05)
    print(p)
    dict = {}
    for c in customers:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    for d, count in dict.items():
        print("Dict: ",d)
        print("Count: ",count)
        if count >= p:
            arr.append(d)
    return arr

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

print(mostActive(arr))
