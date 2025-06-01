#not working solution, keeping this so that I can review my mistake later, will see solution now
def solution(n,arr):
    b = []
    c = []
    pos = []
    for i in range(n):
        for j in range(n):
            if i==j or arr[j] == -200 or arr[i] == -200:
                continue
            if arr[j]%arr[i] == 0:
                b.append(arr[i])
                pos.append(i)
                break
    if len(b) == 0 and len(c) == 0:
        b = arr[0:1]
        c = arr[1:]
    elif len(b) > 0 and len(b) < len(arr):
        for i in range(n):
            if i in pos:
                continue
            c.append(arr[i])
        
    if len(b) == 0 or len(c) == 0:
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
        else:
            print(f"{len(b)} {len(c)}")
            print(' '.join(map(str, b)))
            print(' '.join(map(str, c)))
        i += 2

if __name__ == "__main__":
    main()