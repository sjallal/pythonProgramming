# To run this script hit "ctrl+shift+b".

f = open("D:/pythonProgramming/LearningPython/Data.txt")
n = int(f.readline())
# b = f.readline()
# print(type(b))
a = []
b = []
for i in range(n):
    b = f.readline().split()
    a.append(b)
    b = []
print(a)
f.close()
