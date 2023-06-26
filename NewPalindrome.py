t = int(input())
for _ in range(t):
    s = input()
    if len(s)%2 == 1:
        mid = len(s)//2 
        before = sorted(s[:mid])
        after =  sorted(s[mid+1:])
        if len(set(before)) == 1 or len(set(after)) == 1:
            print("NO")
        else: 
            for i in range(len(before)):
                if before[i] == after[i]:
                    continue
                else:
                    print("NO")
                    break
            print("YES")   
    else:
        mid = len(s)//2 
        before = sorted(s[:mid])
        after =  sorted(s[mid:])
        if len(set(before)) == 1 or len(set(after)) == 1:
            print("NO")
        else: 
            for i in range(len(before)):
                if before[i] == after[i]:
                    continue
                else:
                    print("NO")
                    break
            print("YES") 
           