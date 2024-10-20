def split_array(input, size):
    # Calculate the total sum of the array
    total_sum = sum(input)
    
    # If the total sum is odd, we can't split it into two equal sums
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    
    # Initialize sums of groups
    g1_sum = 0
    g2_sum = 0
    g3 = []
    
    # Distribute elements into groups
    for i in input:
        if i % 5 == 0:
            g1_sum += i
        elif i % 3 == 0:
            g2_sum += i
        else:
            g3.append(i)
    
    # Calculate the needed balance to make both groups equal
    needed_sum = target_sum - g1_sum
    if needed_sum < 0:
        needed_sum = -needed_sum  # Convert to positive if necessary
    
    # Dynamic programming to check if we can form needed_sum from g3
    def can_sum(arr, target):
        # DP array to check if a subset with sum `target` is possible
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in arr:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        
        return dp[target]
    
    # Check if the balance can be achieved with the remaining elements
    if can_sum(g3, needed_sum):
        return True
    else:
        return False

def main():
    size = int(input())
    input_array = list(map(int, input().split()))

    if split_array(input_array, size):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
