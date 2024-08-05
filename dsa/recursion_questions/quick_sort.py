"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def partition(arr: List[int], low: int, high: int):
    
    piviot = arr[high]
    i = low-1
    
    for j in range(low, high):
        
        if arr[j] <= piviot:
            
            # i yha pr piviot se bda element hold krk rkha hoga toh aur j iterator h toh hme i,j swap krne h kyu k hme pivot se bde elemt end me chahiye
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    
            

        
        

def quickSort(arr: List[int], low: int, high: int):
    if low < high:
        
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    

l = [6,11,3,5,6,12,9,7,8]
quickSort(l,0,8)
print(l)