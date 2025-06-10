def solution(n,k,x):
    mins = (k*(k+1))//2
    maxs = ((n*(n+1))//2) - (((n-k)*(n-k+1))//2)
    if x>=mins and x<=maxs:
        return "YES"
    return "NO"
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n,k,x = map(int,lines[i].split())
        print(solution(n,k,x))
        i += 1

if __name__ == "__main__":
    main()