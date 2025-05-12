def IntersectionTwoArr(arr1,arr2):
    i=j=0
    n,m=len(arr1), len(arr2)
    res=[]
    while i<n and j<m:
        if arr1[i] == arr2[j]:
            if res:
                if res[-1]==arr1[i]:
                    i+=1
                    j+=1
                    continue
            res.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return res if res else [-1]
