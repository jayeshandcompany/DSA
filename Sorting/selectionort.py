def selectionSort(arr):
    for i in range(len(arr)):
        m=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[m]:
                m=j
        arr[m], arr[i] = arr[i], arr[m]
    return arr
print(selectionSort([3,24,53,11,1,1,0 ]))