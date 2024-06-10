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