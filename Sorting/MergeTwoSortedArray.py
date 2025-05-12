def MergeTwoSortedArray(arr1, arr2):
    res=[]
    i,j,n,m = 0, 0, len(arr1), len(arr2)
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<n:
        res.append(arr1[i])
        i+=1
    while j<m:
        res.append(arr2[j])
        j+=1
    return res
print(MergeTwoSortedArray([1,2,3,4],[0,1,2,6,7]))