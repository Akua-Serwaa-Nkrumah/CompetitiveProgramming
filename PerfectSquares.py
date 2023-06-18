import math
 
def is_perfect_square(n):
    return math.sqrt(n)**2 == n
max_num = float('-inf')
m = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
for i in range(m-1,-1,-1):
    if is_perfect_square(arr[i]) != True:
        print(arr[i])
        break
    else:
        max_num = arr[i]
        max(max_num,arr[i])
        print(max_num)
# max_value = float('-inf')  # Initialize the maximum value as negative infinity
# for num in arr:
#     if math.isqrt(num) ** 2 != num:  # Check if the number is not a perfect square
#         max_value = max(max_value, num)

# print(max_value)
