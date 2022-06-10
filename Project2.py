adad = str(input())
adad_list = list(adad)
list1 = []
list2 = []
i = 0
n = 0
result = ''

x = len(adad_list)

for item in adad_list:
    if x == 1:
        list1.append(x)
        list1.append(item)
    else:
        if i < x-1:
            if item == adad_list[i+1]:
                list2.append(item)

            elif item != adad_list[i+1]:
                list2.append(item)
                n = len(list2)
                list1.append(n)
                list1.append(item)
                n = 0
                list2.clear()

        if i == x-1:
            if item == adad_list[x-2]:
                list2.append(item)
                n = len(list2)
                list1.append(n)
                list1.append(item)
                n = 0
                list2.clear()

        i = i + 1

for item in list1:
    result += str(item)

print(result)