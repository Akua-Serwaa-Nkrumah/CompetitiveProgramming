n = int(input())
print(2)
for i in range(n):
    print(*" "*(n-i), *range(i), *range(i, -1, -1))

for i in range(n, -1, -1):
    print(*" "*(n-i), *range(i), *range(i, -1, -1))
