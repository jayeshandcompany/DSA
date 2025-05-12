def UnionTwoArr(arr1, arr2):
    i=j=0
    n=len(arr1)
    m=len(arr2)
    res=[]
    while i<n and j<m:
        if res:
            if res[-1]==arr1[i]:
                i+=1
                continue
            if res[-1]==arr2[j]:
                j+=1
                continue

        if arr1[i]<=arr2[j]:
            x=arr1[i]
            res.append(x)
            i+=1
            if arr1[i-1] == arr2[j]:
                j+=1
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
print(UnionTwoArr([1,1,2,4,5],[1,1,3,4,6]))
