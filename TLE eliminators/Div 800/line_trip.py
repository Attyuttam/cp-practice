def solution(n, k, arr):
    last = 0
    vol = 0
    for i in range(n):
        vol = max(vol, arr[i]-last)
        last = arr[i]
    vol = max(vol, (k - arr[n-1])*2)
    return vol
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n, k = map(int, lines[i].split())
        arr = list(map(int, lines[i+1].split()))
        print(solution(n, k, arr))
        i+=2

if __name__ == "__main__":
    main()
