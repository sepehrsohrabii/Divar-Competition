projectInput = input()
numbersStr = ''
numberList = []

for item in list(projectInput):
    if item.isdigit():
        numbersStr += item
    else:
        numbersStr += ' '

numbersList = [int(s) for s in numbersStr.split() if s.isdigit()]
number = ''
numbers = []
for item in numbersList:
    item = str(item)
    n = 0
    x = len(item)
    for n in range(x-1):
        number = item[n] + item[n+1]
        numbers.append(number)

# Program to check if a number is prime or not
for num in numbers:
    num = int(num)
    flag = False
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if not flag:
        print(num)

