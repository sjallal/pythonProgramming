"""
Sample Input
5
5 4 3 4 5
Sample Output
8

Explanation
We can compute the following:
IndexProduct(1) = 0x0 = 0
IndexProduct(2) = 1x5 = 5
IndexProduct(3) = 2x4 = 8
IndexProduct(4) = 1x5 = 5
IndexProduct(5) = 0x0 = 0

The largest of these is 8, so it is the answer.
"""

def solve(a):
    l = len(a)
    maxProd = 0
    for i in range(l):
        j = i - 1
        k = i + 1
        print(i, end=' ')

        while(j >= 0):
            if(a[i] < a[j]):
                break
            j -= 1
        print(j, end=' ')
        if(j < 0):
            j = 0
        elif(a[i] < a[j]):
            j += 1
        else:
            j = 0

        while(k < l):
            if(a[i] < a[k]):
                break
            k += 1
        print("k", k)
        if(k == l):
            k = 0
        elif(a[i] < a[k]):
            k += 1
        else:
            k = 0

        prod = j * k
        if(maxProd < prod): maxProd = prod
        # print(i,j,k)
    return maxProd

n = int(input())
arr = input().split()
for _ in range(n):
    arrInt = [int(i) for i in arr]
print(solve(arrInt))
