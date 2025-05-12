def MergeSort(arr, l, r):
    if r>l:
        m=(l+r)//2
        MergeSort(arr,l,m)
        MergeSort(arr,m+1,r)
        Merge(arr,l,m,r)
def Merge(arr,l,m,r):
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    i=j=0
    k=l
    a=len(left)
    b=len(right)
    while i<a and j<b:
        if left[i]<=right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]= right[j]
            j+=1
            k+=1
    while i<a:
        arr[k]=left[i]
        i+=1
        k+=1
    while j<b:
        arr[k]=right[j]
        j+=1
        k+=1
arr=[2,44,1,34,23,34,5,1]
MergeSort(arr,0, 7)
print(*arr)

                
    