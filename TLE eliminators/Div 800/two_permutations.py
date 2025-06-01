def solution(n,a,b):
    if n==a and n==b:
        return "Yes"
    if a+b>n:
        return "No"
    x = n - (a+b)
    if x<=1:
        return "No"
    return "Yes"
    
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n,a,b = map(int, lines[i].split())
        print(solution(n,a,b))
        i+=1

if __name__ == "__main__":
    main()