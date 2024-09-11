def maximumProfit(arr):
    temp = []
    
    for i in arr:
        count = 0
        for j in range(len(arr)):
            if arr[j] >= i:
                count += 1
        temp.append(count*i)
    return max(temp)

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)


# 4
# 30 20 53 14