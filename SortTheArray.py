def sortArraySegment(n, arr):
    start = -1
    end = -1

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if start == -1:
                start = i
            end = i + 1
    
    if start == -1:
        return "yes\n1 1"  # Array is already sorted
    
    # if start != 0 and n != end:
    #     if arr[end] >= arr[start-1]
    if  end == n-1 or arr[start] <= arr[end + 1] and (arr[end] >= arr[start-1] and start != 0):
        return f"yes\n{start + 1} {end + 1}"
    
    return "no"

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(sortArraySegment(n, arr))
