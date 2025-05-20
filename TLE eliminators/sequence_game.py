def solution(n,arr):
    res = []
    res.append(arr[0])
    
    for i in range(1,n):
        if arr[i] >= res[len(res)-1]:
            res.append(arr[i])
        else:
            res.append(arr[i]-1) if arr[i]-1>0 else res.append(arr[i])
            res.append(arr[i])
    return res
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        res = solution(n,arr)
        print(len(res))
        print(' '.join(map(str, res)))
        i += 2

if __name__ == "__main__":
    main()