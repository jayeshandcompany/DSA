def getInvCount(arr):
    return MergeSort(arr,0,len(arr))
def MergeSort(arr,low,high, inv_count=0):
    if high>low:
        mid= (high+low)//2
        inv_count += MergeSort(arr,low,mid, inv_count)
        inv_count += MergeSort(arr,mid+1,high, inv_count)
        inv_count += Merge(arr,low,mid,high)
    return inv_count
def Merge(arr,l,m,h):
    left = arr[l:m]
    right = arr[m+1:h+1]
    i = j = 0
    k = l
    a=len(left)
    b=len(right)
    c=0
    while i<a and j<b:
        if left[i]<= right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            c+= (m-i)+1
            j+=1
            k+=1
    return c
print(getInvCount([1,2,11,3,4,2]))    
    