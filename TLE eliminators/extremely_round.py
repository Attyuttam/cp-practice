def solution(n):
    c = 0
    while n>=10:
        c+=1
        n = n//10
    
    return c*9 + n
    
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        print(solution(n))
        i+=1

if __name__ == "__main__":
    main()