def RemoveSmallest(arr):
    compare = [0]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(arr[i]-arr[j]) == 1:
                minimum = min(arr[i],arr[j])
                min_index = arr.index(minimum)
                if compare[min_index] == 0:
                    compare[min_index] = minimum
              
    if compare.count(0) == 1:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(RemoveSmallest(arr))