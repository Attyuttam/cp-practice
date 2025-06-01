def solution(n, arr):
    i = 0
    a = 0
    while i<n:
        if arr[i] == ".":
            if i-1>=0 and i+1<n and arr[i-1] == "." and arr[i+1] == ".":
                return 2
            else:
                a+=1
        i+=1
    return a
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = list(lines[i+1])
        print(solution(n, arr))
        i+=2

if __name__ == "__main__":
    main()
