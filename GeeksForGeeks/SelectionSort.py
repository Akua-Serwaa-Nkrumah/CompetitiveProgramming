#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        selected = arr[i]
        return selected
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index = i
            
            for j in range(i+1,n):
                if arr[min_index] > arr[j]:
                    min_index = j
                    
            arr[i], arr[min_index] = arr[min_index], arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends