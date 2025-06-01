def solution(x1,y1,x2,y2):
    if y2 < y1:
        return "-1"
    if y2 < y1 + x2 - x1:
        return "-1"
    #to find (p,q)
    q = y1
    p = y1 - y2 + x2
    
    return str(abs(x1-p) + abs(y2-q))
    

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        a,b,c,d = map(int, lines[i].split())
        print(solution(a,b,c,d))
        i+=1

if __name__ == "__main__":
    main()