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

### Selection Sort  (select the minimum element and swap)

[13,4,9,5,3] 

make two pointers assumed_min,actual_min start with making assumed min as arr[i] "13" then compare it to find min make the min "3" as acctual_min and now swap them so 3 will be at the first index and 13 will be at last 

increment i do previous step for arr[i] means 4 will not be swapped 

increment i do previous step for arr[i] means 9 will be swapped to 5 in this way sorting happen 

Name because of card selction algo




# Insertion Sort cards wala: Pseudocode, Python Implementation, and Analysis

## Pseudocode Steps
1. **Start from the second element**: Assume the first element is already sorted.
2. **Pick the current element** (say `key`) and compare it with the elements before it.
3. **Shift elements**: If the element before the `key` is greater, move it one position ahead.
4. **Insert the key** into its correct position in the sorted sub-array.
5. **Repeat** until the entire array is sorted.

## Pseudocode
```
for i from 1 to length(array):
    key = array[i]
    j = i - 1
    
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j = j - 1
    
    array[j + 1] = key
```

## Python Implementation
```
def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
```

## Analysis

- **Time Complexity**:
  - **Best Case**: O(n) – When the array is already sorted, the inner loop doesn't run.
  - **Worst Case**: O(n^2) – When the array is sorted in reverse order, the inner loop runs `i` times for each element.
  - **Average Case**: O(n^2) – On average, the algorithm will take O(n^2) operations as half of the elements will need to be compared and possibly shifted.

- **Space Complexity**: O(1) – Insertion sort is an in-place sorting algorithm, meaning it requires a constant amount of additional space.

- **Stability**: Insertion sort is stable, meaning that it preserves the relative order of elements with equal values.

- **Adaptive**: Insertion sort is adaptive, meaning that it can take advantage of existing order in the array (e.g., it performs better on nearly sorted arrays).

- **Use Cases**: It’s efficient for small data sets or arrays that are nearly sorted, and it’s often used as the final stage of more complex algorithms like Timsort.
```

You can save this as a `.md` file and view it with any Markdown viewer.