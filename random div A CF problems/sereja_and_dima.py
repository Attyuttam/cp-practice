from collections import Counter

def solution(n, arr):
    i = 0
    j = n-1
    
    s = 0
    d = 0
    
    m = 1
    while i<=j:
        if m%2 != 0:
            if arr[i]>arr[j]:
                s+=arr[i]
                i+=1
            else:
                s+=arr[j]
                j-=1
        else:
            if arr[i]>arr[j]:
                d+=arr[i]
                i+=1
            else:
                d+=arr[j]
                j-=1
        m+=1
    print(f"{s} {d}")
        
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    solution(n,arr)
    

if __name__ == "__main__":
    main()
