def MergeSubArray(arr,low,mid,high):
    left= arr[low:mid+1]
    right= arr[mid+1:high]
    i,j,k,n,m=0,0,0,mid-low,high-(mid+1)
    while i<n and j<m:
        if left[i]<=right[j]:
            arr[low+k]=left[i]
            i+=1
            k+=1
        else:
            arr[low+k]=right[j]
            j+=1
            k+=1
    while i<n:
        arr[k] = left[i]
        i+=1
        k+=1
    while j<m:
        arr[k] = right[j]
        j+=1
        k+=1
    return arr
print(MergeSubArray([1,2,3,5,2,3,4],0,3,7))
