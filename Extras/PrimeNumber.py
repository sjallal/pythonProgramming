def isPrime(n):
    if n % 2 is 0:
        return False
    s = math.floor(math.sqrt(n))
    for i in range(s, 1, -1):
        if n % i is 0:
            return False
    return True
