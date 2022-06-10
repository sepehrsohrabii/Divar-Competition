personTimesList = []
def epochs():
    user_id = input()
    busy_day = input()
    n = int(input())
    inputList = []
    inputs = []
    for x in range(n):
        inputs = input().split(' ')
        i = inputs[0]
        day_name = [1]
        start_epoch = inputs[2]
        end_epoch = inputs[3]
        inputList.append({
            'day_name': day_name,
            'start_epoch': start_epoch,
            'end_epoch': end_epoch
        })

    t = 0
    inputList_len = len(inputList)
    personTimesList.append({
        'user_id': user_id,
        'busy_day': busy_day,
        'inputList': inputList,
    })

    return personTimesList


def intersections(a,b):
    ranges = []
    i = j = 0
    while i < len(a) and j < len(b):
        a_left, a_right = a[i]
        b_left, b_right = b[j]

        if a_right < b_right:
            i += 1
        else:
            j += 1

        if a_right >= b_left and b_right >= a_left:
            end_pts = sorted([a_left, a_right, b_left, b_right])
            middle = [end_pts[1], end_pts[2]]
            ranges.append(middle)

    ri = 0
    while ri < len(ranges)-1:
        if ranges[ri][1] == ranges[ri+1][0]:
            ranges[ri:ri+2] = [[ranges[ri][0], ranges[ri+1][1]]]

        ri += 1

    return ranges

person = input()
h = 0
sepehr = []
while h < int(person):

    sepehr.append(epochs())

   # result = 0
   # for item in intersections(a, b):
   #     start = int(item[0])
   #     end = int(item[1])
   #     result1 = end - start
   #     result = result + result1

   # print(result)
    h =+ 1
meeting_id = input()
duration = input()