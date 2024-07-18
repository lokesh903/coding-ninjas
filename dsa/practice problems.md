Patterns 
1. https://classroom.codingninjas.com/app/classroom/me/30679/content/760319/offering/12699226/problem/969
2. https://classroom.codingninjas.com/app/classroom/me/30679/content/760319/offering/12699227/problem/671

### 3. Move Zero to lowest index

You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra array/list.

```
Sample Input 1:
1
7
0 1 1 0 1 0 1
Sample Output 1:
0 0 0 1 1 1 1
Sample Input 2:
2
8
1 0 1 1 0 1 0 1
5
0 1 0 1 0
Sample Output 2:
0 0 0 1 1 1 1 1
0 0 0 1 1 
```

Solution maintian the lowest position where zero can be placed 
```
def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    pointer = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[pointer],arr[i] = arr[i],arr[pointer]
            pointer+=1
```

