def bubbleSort(arr):
    for i in range(1,len(arr)):
        Change = False
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                Change = True
        if Change:
            continue 
        else:
            break
    return arr
print(bubbleSort([4,22,5,6,78,2,1]))
            