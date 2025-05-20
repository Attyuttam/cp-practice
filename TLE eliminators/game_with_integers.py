def solution(n):
    if int(n%3) == 0:
        return "Second"
    return "First"
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    for i in range(1,t+1):
        n = int(lines[i])
        print(solution(n))

if __name__ == "__main__":
    main()