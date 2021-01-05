list1 = [11,22,11,33,44,22,44,33,11,22]
dict_count = {}
for data in list1:
    if data in dict_count:
        dict_count[data] += 1
    else:
        dict_count[data] = 1
    print(data, dict_count)
print(dict_count)