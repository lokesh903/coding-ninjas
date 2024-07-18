### Selection sort

```
def selectionSort(arr: List[int]) -> None: 
     for i in range (len(arr)-1):
          mp = i
          for j in range(i+1,len(arr)):
               if arr[mp] > arr[j]:
                    mp = j
          arr[mp],arr[i] = arr[i],arr[mp]        
```

### Insertion sort

```
def insertionSort(arr):
    # write your code here 
    for i in range (1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1] 
    pass
```

### Merging two sorted lists

```
def merge(arr1, n, arr2, m) : 
    arr3=[]
    arr1_ind,arr2_ind = 0,0
    while (arr1_ind+arr2_ind<n+m):
        if(arr1_ind>=n):
            arr3.extend(arr2[arr2_ind:])
            return arr3
        if(arr2_ind>=m):
            arr3.extend(arr1[arr1_ind:])
            return arr3
        a1e = arr1[arr1_ind]
        a2e = arr2[arr2_ind]
        if(a1e<a2e):
            arr3.append(a1e)
            arr1_ind+=1
        elif(a2e<a1e):
            arr3.append(a2e)
            arr2_ind+=1
        else:
            arr3.extend([a1e]*2)
            arr2_ind+=1
            arr1_ind+=1
    return arr3
        
    # write your code here 
    pass
```

### push zeros to end
```
def pushZerosAtEnd(arr, n) :
    #Your code goes here
    p = 0
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[i],arr[p]=arr[p],arr[i]
            p+=1
```