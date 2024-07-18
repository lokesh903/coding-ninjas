def merge(arr:[int], l:int,mid:int, r: int):
    lenOfLeft = mid - l  + 1
    lenOfRight = r - mid

    right, left = arr[mid+1:r+1], arr[l:mid+1] 

    # merging
    indr = 0
    indl = 0
    inda = l
    while(indr < lenOfRight   or indl < lenOfLeft ):
        if indr >= lenOfRight:
            
            # append left array into original
            while(indl<lenOfLeft):
                arr[inda] = left[indl]
                indl+=1
                inda+=1
        elif indl >= lenOfLeft:
            while(indr < lenOfRight):
                arr[inda] = right[indr]
                indr+=1
                inda+=1
        elif right[indr] < left[indl]:
            arr[inda] = right[indr]
            indr+=1
            inda+=1
        else:
            arr[inda] = left[indl]
            indl+=1
            inda+= 1


def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if r <= l:  
        return
    mid = l + (r-l)//2
    # left part
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)
    pass
a= [2,13,4,1,3,6,28]
mergeSort(a,0,6)
print(a)