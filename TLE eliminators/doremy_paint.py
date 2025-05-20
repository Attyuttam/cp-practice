from collections import defaultdict
import math
def solution(n, arr):
    if n == 1 or n==2:
        return "Yes"
    d = defaultdict(int)
    for a in arr:
        d[a]+=1
    if len(d) == 1:
        return "Yes"
    if len(d) > 2:
        return "No"
    
    v1 = list(d.items())[0][1]
    v2 = list(d.items())[1][1]
    
    if n%2 == 0:
        if v1==v2:
            return "Yes"
    else:
        if v1 == v2+1 or v2 == v1+1:
            return "Yes"
    return "No"

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n, arr))
        i += 2

if __name__ == "__main__":
    main()