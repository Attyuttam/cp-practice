def solution(n,arr):
    np = 0
    nn = 0
    for v in arr:
        if v == 1:
            np+=1
        else:
            nn+=1
    
    res = 0
    while nn > np or nn%2 != 0:
        nn-=1
        np+=1
        res+=1
    return res
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i].strip())
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n,arr))
        i+=2

if __name__ == "__main__":
    main()