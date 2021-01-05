import math

p_same = float(input())

n = math.ceil(math.sqrt(2 * 365 * math.log(1 / (1-p_same))))

print(n)
