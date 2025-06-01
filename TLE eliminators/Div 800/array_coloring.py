def solution(n,arr):
    return "YES" if sum(arr)%2 == 0 else "NO"
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        res = solution(n,arr)
        print(res)
        i += 2

if __name__ == "__main__":
    main()