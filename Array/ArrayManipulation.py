"""
Sample Input
5 3
1 2 100
2 5 100
3 4 100
Sample Output
200

Explanation:-
After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be 200.

Sample Input
5 3
2 4 7
1 3 1
3 5 13
Sample Output
21
"""


n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    x -= 1
    y -= 1
    list[x] += incr
    list[y+1] -= incr;

max = sum = 0
for i in arr:
    sum = sum + i
    if(max < sum): max = sum
print(max)
