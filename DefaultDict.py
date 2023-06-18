from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
B = defaultdict(list)

for i in range(1,n+1):
    A[input()].append(i)
for j in range(1,m+1):
    B[input()].append(j)

for key in B:
    if key in A:
        print(*A[key])
    else:
        print(-1)