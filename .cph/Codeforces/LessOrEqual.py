def LessOrEqual():
    n, k = map(int,input().split())
    numbers = sorted(map(int,input().split()))
    check = []
    for i in range(k):
        check.append(numbers[i])
        numbers[i] = -1
    # print(numbers)   
    if len(numbers) == 1 and numbers[0]== 0 and k == 0:
        return 1 
    for number in numbers[k:]:
        if len(check) == 0:
            return -1
        if number <= check[-1]:
            return -1      
    return(check[-1])
print(LessOrEqual())  

# n, k = map(int,input().split())
# numbers = sorted(map(int,input().split()))
 
# check = []
# for i in range(n):
#     if numbers[i] <= k + 1:
#         check.append(numbers[i])
# if len(check) == k:
#     print(k+1)
# else: 
#     print(-1)