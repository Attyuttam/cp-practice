def solution(n,arr):
    maxv = max(arr)
    minv = min(arr)
    sum = maxv + minv
    
    res = []
    for a in arr:
        res.append(sum - a)
    return ' '.join(map(str,res))
        

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