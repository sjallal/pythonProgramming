class Inventory:
    def __init__(self, iphone, iphonePrice, ipod, ipodPrice):
        self.iphone = iphone
        self.iphonePrice = iphonePrice
        self.ipod = ipod
        self.ipodPrice = ipodPrice


brazil = Inventory(100, 100, 100, 65)
argentina = Inventory(50, 150, 100, 100)

inp = input().split(":")

purchaseLoc = inp[0]
passport = inp[1]
iphoneReq = 0
ipodRed = 0
totalCost = 0
flag = True

if inp[2] == "IPHONE":
    iphoneReq = int(inp[3])
    ipodReq = int(inp[5])
else:
    iphoneReq = int(inp[5])
    ipodReq = int(inp[3])

if iphoneReq > brazil.iphone + argentina.iphone or ipodReq > brazil.ipod + argentina.ipod:
    print("OUT_OF_STOCK:"+str(brazil.ipod)+":"+str(argentina.ipod)+":"+str(brazil.iphone)+":"+str(argentina.iphone))
    flag = False

elif purchaseLoc[0] == 'B' and passport[0] == 'B':
    if brazil.iphone >= iphoneReq:
        totalCost += iphoneReq * brazil.iphonePrice
        brazil.iphone -= iphoneReq
    else:
        totalCost += brazil.iphone * brazil.iphonePrice
        iphoneReq -= brazil.iphone
        brazil.iphone = 0
        totalCost += (iphoneReq * argentina.iphonePrice) + (400 * ((iphoneReq//10)+1))
        argentina.iphone -= iphoneReq
    if brazil.ipod >= ipodReq:
        totalCost += ipodReq * brazil.ipodPrice
        brazil.ipod -= ipodReq
    else:
        totalCost += brazil.ipod * brazil.ipodPrice
        ipodReq -= brazil.ipod
        brazil.ipod = 0
        totalCost += (ipodReq * argentina.ipodPrice) + (400 * ((ipodReq//10)+1))
        argentina.ipod -= ipodReq
elif purchaseLoc[0] == 'B' and passport[0] == 'A':
    if brazil.iphone >= iphoneReq:
        totalCost += iphoneReq * brazil.iphonePrice
        brazil.iphone -= iphoneReq
    else:
        totalCost += brazil.iphone * brazil.iphonePrice
        iphoneReq -= brazil.iphone
        brazil.iphone = 0
        totalCost += (iphoneReq * argentina.iphonePrice) + (320 * ((iphoneReq//10)+1))
        argentina.iphone -= iphoneReq
    if brazil.ipod >= ipodReq:
        totalCost += ipodReq * brazil.ipodPrice
        brazil.ipod -= ipodReq
    else:
        totalCost += brazil.ipod * brazil.ipodPrice
        ipodReq -= brazil.ipod
        brazil.ipod = 0
        totalCost += (ipodReq * argentina.ipodPrice) + (320 * ((ipodReq//10)+1))
        argentina.ipod -= ipodReq
elif purchaseLoc[0] == 'A' and passport[0] == 'A':
    if brazil.iphone >= iphoneReq:
        if iphoneReq % 10 > 7:
            totalCost += (iphoneReq * brazil.iphonePrice) + ((iphoneReq // 10) + 1) * 400
            brazil.iphone -= (iphoneReq - iphoneReq % 10)
        else:
            totalCost += ((iphoneReq - iphoneReq % 10) * brazil.iphonePrice) + ((iphoneReq - iphoneReq % 10) // 10) * 400
            brazil.iphone -= (iphoneReq - iphoneReq % 10)
            totalCost += (iphoneReq % 10) * argentina.iphonePrice
            argentina.iphone -= (iphoneReq % 10)
    else:
        totalCost += (brazil.iphone * brazil.iphonePrice) + (brazil.iphone // 10) * 400
        iphoneReq -= brazil.iphone
        brazil.iphone = 0
        totalCost += iphoneReq * argentina.iphonePrice
        argentina.iphone -= iphoneReq
    if argentina.ipod >= ipodReq:
        totalCost += ipodReq * argentina.ipodPrice
        argentina.ipod -= ipodReq
    else:
        totalCost += argentina.ipod * argentina.ipodPrice
        ipodReq -= argentina.ipod
        argentina.ipod = 0
        totalCost += (ipodReq * brazil.ipodPrice) + (320 * ((ipodReq//10)+1))
        brazil.ipod -= ipodReq
elif purchaseLoc[0] == 'A' and passport[0] == 'B':
    if brazil.iphone >= iphoneReq:
        if iphoneReq % 10 > 6:
            totalCost += (iphoneReq * brazil.iphonePrice) + ((iphoneReq // 10) + 1) * 320
            brazil.iphone -= (iphoneReq - iphoneReq % 10)
        else:
            totalCost += ((iphoneReq - iphoneReq % 10) * brazil.iphonePrice) + ((iphoneReq - iphoneReq % 10) // 10) * 320
            brazil.iphone -= (iphoneReq - iphoneReq % 10)
            totalCost += (iphoneReq % 10) * argentina.iphonePrice
            argentina.iphone -= (iphoneReq % 10)
    else:
        totalCost += (brazil.iphone * brazil.iphonePrice) + (brazil.iphone // 10) * 320
        iphoneReq -= brazil.iphone
        brazil.iphone = 0
        totalCost += iphoneReq * argentina.iphonePrice
        argentina.iphone -= iphoneReq
    if brazil.ipod >= ipodReq:
        totalCost += ((ipodReq - (ipodRed % 10)) * brazil.ipodPrice) + ((ipodReq - (ipodRed % 10)) // 10) * 320
        brazil.ipod -= (ipodReq - (ipodRed % 10))
        totalCost += (ipodRed % 10) * argentina.ipodPrice
        argentina.ipod -= ipodReq % 10
    else:
        totalCost += (brazil.ipod * brazil.ipodPrice) + (320 * (brazil.ipod // 10))
        ipodReq -= brazil.ipod
        brazil.ipod = 0
        totalCost += (ipodReq * argentina.ipodPrice)
        argentina.ipod -= ipodReq

if flag:
    print(str(totalCost)+":"+str(brazil.ipod)+":"+str(argentina.ipod)+":"+str(brazil.iphone)+":"+str(argentina.iphone))


'''

INPUT 1:
BRAZIL:B123AB1234567:IPHONE:20:IPOD:10
OUTPUT 1:
2650:90:100:80:50

INPUT 2:
ARGENTINA:B123AB1234567:IPHONE:22:IPOD:10
OUTPUT 2:
3910:90:100:80:48

INPUT 3:
BRAZIL:AAB123456789:IPHONE:125:IPOD:70
OUTPUT 3:
19260:30:100:0:25

INPUT 4:
ARGENTINA:AAB123456789:IPOD:50:IPHONE:25
OUTPUT 4:
8550:100:50:80:45

INPUT 5:
BRAZIL:IPHONE:50:IPOD:150
OUTPUT 5:
18500:0:50:50:50

INPUT 6:
BRAZIL:IPHONE:250:IPOD:150
OUTPUT 6:
OUT_OF_STOCK:100:100:100:50

'''

