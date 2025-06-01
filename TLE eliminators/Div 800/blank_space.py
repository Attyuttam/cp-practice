def solution(n,arr):
    lo = -1
    i = 1
    
    maxLen = -1
    for i in range(0,n):
        if arr[i] == 1:
            maxLen = max(maxLen, i-lo-1)
            lo = i
    maxLen = max(maxLen, n-lo-1)
    return maxLen
            
    
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i].strip())
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n,arr))
        i+=2

if __name__ == "__main__":
    main()