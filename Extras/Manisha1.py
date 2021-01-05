# n = int(input())
# lis = input().split(" ")
#
# for s in lis:
#     t = 0
#     for i in s:
#         t += int(i)
#     print(t, end=" ")

'''

4
43 345 20 987

'''

string = input()

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',' ')
for c in string:
    if c in vowels:
        string = string.replace(c, "")
print(string)

'''

haveaniceday
hvncdy

'''