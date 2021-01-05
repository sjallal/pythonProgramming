# import math
t = int(input())
while(t > 0):
    n = int(input())
    i = 0
    while(2 ** i <= n):
        i += 1
    print(i)
    t -= 1
