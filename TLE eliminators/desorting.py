def solution(n,arr):
    isSorted = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            isSorted = False
            break
    if not isSorted:
        return 0
        
    minv = float('inf')
    pos1 = 0
    pos2 = 0
    for i in range(1,n):
        if arr[i] >= arr[i-1] and arr[i] - arr[i-1] < minv:
            minv = arr[i] - arr[i-1]
            pos1 = i-1
            pos2 = i            
    #print(pos1,pos2)
    return 1 if arr[pos1] == arr[pos2] else ((arr[pos2] - arr[pos1])//2 + 1)
        
        

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
        print(res)
        i += 2

if __name__ == "__main__":
    main()