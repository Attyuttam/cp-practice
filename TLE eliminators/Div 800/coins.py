def solution(n,k):
    if k%2 == 0:
        if n%2!=0:
            return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n,k = map(int, lines[i].split())
        print(solution(n,k))
        i+=1

if __name__ == "__main__":
    main()