def min_eff(pat, doc, eff, divide):
    for e in eff[0]:
        pass
    return 0

p, d = [int(i) for i in input().split()]
effort = []
for i in range(d):
    temp = []
    temp = [int(i) for i in input().split()]
    effort.append(temp)
res = 0
for i in range(p):
    x = min_eff(p, d, effort, i)
    if x < res:
        res = x
# print(effort[0][0])



'''
4 2
2 2 2 2
3 1 2 3
'''