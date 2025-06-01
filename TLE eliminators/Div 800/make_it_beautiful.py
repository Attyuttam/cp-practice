def solution(n,arr):
    all_el_same = True
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            all_el_same = False
            break
            
    if all_el_same:
        print("NO")
        return
    
    if n == 2:
        print("YES")
        print(' '.join(map(str,arr)))
        return
    
    arr = sorted(arr, reverse=True)
    
    if arr[0] == arr[1]:
        pos = -1
        for i in range(2,n):
            if arr[i]!=arr[0]:
                pos = i
                break
        
        temp = arr[1]
        arr[1] = arr[pos]
        arr[pos] = temp
        
    print("YES")
    print(' '.join(map(str,arr)))
    
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = list(map(int, lines[i+1].split()))
        solution(n,arr)
        i+=2

if __name__ == "__main__":
    main()