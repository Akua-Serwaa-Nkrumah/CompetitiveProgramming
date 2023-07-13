# def LessOrEqual():
#     n, k = map(int,input().split())
#     numbers = sorted(map(int,input().split()))
#     check = []
#     for i in range(k):
#         check.append(numbers[i])
#         numbers[i] = -1
        
#     if k > len(numbers):
#         return -1
    
#     for number in numbers[k:]:
#         if number in check:
#             return -1
#     print(numbers.count(numbers[0]))
# print(LessOrEqual())  

array = [2,"3",5]
print(array)



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