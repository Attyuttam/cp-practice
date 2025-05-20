def solution(xn,sn,x,s):
    if len(x) >= len(s):
        if s in x:
            return 0
        elif s in (x+x):
            return 1
        return -1
    c = 0
    while len(x) <= 25:
        if s in x:
            return c
        x = x + x
        c += 1
    return -1 if s not in x else c
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        xn, sn = map(int, lines[i].split())
        x = lines[i+1]
        s = lines[i+2]
        print(solution(xn,sn,x,s))
        i += 3

if __name__ == "__main__":
    main()