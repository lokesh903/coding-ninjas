### Binary Search

1. Initialize variables Lower,Upper,target
2. Calculate midpoint mid = (low+high) //2
3. Compare midpoint to target 
    a. if target == mid 
        return you find the targt its index is the result
    
    b. if target > mid
        `low = mid + 1`
        Goto step 2
    
    c. if target < mid then make 
        `high = mid - 1`
        Goto step 2

4. if you reach the end that means element not found

```def search(nums: [int], target: int):
    # write your code logic !!
    l,u = 0,len(nums)-1
    while(l<=u):
        m = (l+u)//2
        if nums[m]==target:
            return m
        elif(nums[m]>target):
            u=m  - 1  
        else:
            l=m + 1 
    return -1
```

### Selection Sort 

[13,4,9,5,3] 

make two pointers assumed_min,actual_min start with making assumed min as arr[i] "13" then compare it to find min make the min "3" as acctual_min and now swap them so 3 will be at the first index and 13 will be at last 

increment i do previous step for arr[i] means 4 will not be swapped 

increment i do previous step for arr[i] means 9 will be swapped to 5 in this way sorting happen 

Name because of card selction algo
