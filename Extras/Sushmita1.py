n = int(input())

lis = []
res = []
for i in range(n):
    lis1 = [int(x) for x in input().split(" ")]
    lis.append(lis1)

for i in range(len(lis)-1):
    a1 = lis[i][3] - lis[i][1]
    b1 = lis[i][0] - lis[i][2]
    c1 = a1 * lis[i][0] + b1 * lis[i][1]
    for j in range(i+1, len(lis)):
        a2 = lis[j][3] - lis[j][1]
        b2 = lis[j][0] - lis[j][2]
        c2 = a2 * lis[j][0] + b2 * lis[j][1]

        determinant = a1 * b2 - a2 * b1

        if determinant == 0:
            continue
        else:
            x = (b2 * c1 - b1 * c2) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            tup = (x, y)
            res.append(tup)
print(res)
res = set(res)
print(res)
print(len(res))

'''
3
0 3 3 2
1 1 4 5
2 4 5 3

'''