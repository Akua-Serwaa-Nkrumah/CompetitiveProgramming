from collections import Counter
t = int(input())  
for _ in range(t):
    n, c = map(int, input().split())  
    planets = Counter(map(int, input().split()))
    
    print(len(planets))
    print(planets[2])
    print(planets)
    
    
