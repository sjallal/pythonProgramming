import math

def isPrime(i):
    sq = int(math.sqrt(i))
    for j in range(2,sq+1):
        if i % j == 0:
            return False
    return True

def fibo(i, j, n):
    sum = 0
    for o in range(n-2):
        sum = i + j
        i = j
        j = sum
    # print("Answer is : "+str(sum))
    print(sum)


n1, n2 = [int(i) for i in input().split()]

prime1 = []
for i in range(n1,n2+1):
    if isPrime(i):
        prime1.append(i)
# print(len(prime1))
# print(prime1)

# cPrime = []
Prime2 = []
dict = {}
max = 0
for i in prime1:
    for j in prime1:
        if i != j:
            temp = int(str(i)+str(j))
            if temp in dict:
                continue
            else:
                dict[temp] = 1
                # cPrime.append(temp)
                if isPrime(temp):
                    Prime2.append(temp)
                    if(temp > max):
                        max = temp
# print(len(cPrime))
# print(cPrime)

# print(len(Prime2))
# print(Prime2)

m = min(Prime2)
# print(m, max, len(Prime2))
fibo(min(Prime2), max, len(Prime2))
