
n = int(input())
inputList = []
inputs = []
for x in range(n+1):
    if x == n:
        inputs = input().split(' ')
        i = int(inputs[0])
        duration = int(inputs[1])
        inputList.append({
            'i': i,
            'duration': duration
        })
    else:
        inputs = input().split(' ')
        i = inputs[0]
        start_epoch = inputs[1]
        end_epoch = inputs[2]
        inputList.append({
            'i': i,
            'start_epoch': start_epoch,
            'end_epoch': end_epoch
        })

t = 0
inputList_len = len(inputList)
for t in range(inputList_len-1):
    if t == 0:
        start_epoch = 0
        end_epoch = int(inputList[t]['start_epoch'])
    else:
        start_epoch = int(inputList[t-1]['end_epoch'])
        end_epoch = int(inputList[t]['start_epoch'])

    status = int(end_epoch - start_epoch)
    duration = int(inputList[inputList_len-1]['duration'])
    if duration <= status:
        if t == 0:
            start_epoch_result = 0
            end_epoch_result = start_epoch_result + int(inputList[inputList_len - 1]['duration'])
            print(start_epoch_result, end_epoch_result)
            break
        else:
            start_epoch_result = int(inputList[t-1]['end_epoch']) + 1
            end_epoch_result = start_epoch_result + int(inputList[inputList_len-1]['duration'])
            print(start_epoch_result, end_epoch_result)
            break

