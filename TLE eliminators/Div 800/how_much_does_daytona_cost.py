def solution(n,k,arr):
    if k in arr:
        return "YES"
    return "NO"
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n, k = map(int, lines[i].split())
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n,k,arr))
        i += 2

if __name__ == "__main__":
    main()