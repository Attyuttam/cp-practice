def solution(n,arr):
    xorres = arr[0]
    for i in range(1,n):
        xorres^=arr[i]
    
    if n%2 == 0:
        if xorres == 0:
            return "2"
        else:
            return "-1"
    else:
        return xorres    
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n,arr))
        i+=2

if __name__ == "__main__":
    main()