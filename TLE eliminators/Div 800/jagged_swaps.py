def solution(n, arr):
    i = 1
    sum = 0
    minv = arr[0]
    maxv = arr[0]
    while i < n:
        sum += arr[i] - arr[i-1]
        minv = min(minv , arr[i])
        maxv = max(maxv, arr[i])
        i+=1
    if sum > 0:
        if arr[0] == minv and arr[n-1] == maxv:
            return "YES"
        elif minv < arr[0]:
            return "NO"
        elif maxv > arr[n-1] and maxv > arr[0]:
            return "YES"
                
    return "NO"

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n, arr))
        i += 2

if __name__ == "__main__":
    main()