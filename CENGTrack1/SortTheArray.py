def sortArraySegment(n, arr):
    start = 0
    end = 0

    if arr == sorted(arr):
        return (start+1,end+1)
    
    for start in range(n-1):
        if arr[start] > arr[start+1]:
            end = start+1
        if sorted 
    
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
