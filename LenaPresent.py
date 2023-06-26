n = int(input())
for i in range(n):
    print(*" "*(n-i),*range(i),*range(i, -1, -1))

for j in range(n, -1, -1):
    print(*" "*(n-j),*range(j),*range(j, -1, -1))
