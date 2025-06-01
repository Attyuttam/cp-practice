def solution(n,arr):
    b = []
    c = []
    maxv = max(arr)
    
    for a in arr:
        if a != maxv:
            b.append(a)
        else:
            c.append(a)
    
    if len(b) == 0:
        return -1, -1
    return b,c
        
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        b,c = solution(n,arr)
        if b == -1:
            print(b)
            #print("=============")
        else:
            print(f"{len(b)} {len(c)}")
            print(' '.join(map(str, b)))
            print(' '.join(map(str, c)))
            #print("=============")
        i += 2

if __name__ == "__main__":
    main()