def selectionsort(arr):
    for i in range(1, len(arr)):
        x=arr[i]
        j=i-1
        while j>=0 and x<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = x
    return arr
    
print(selectionsort([1,4,2,3,0]))
