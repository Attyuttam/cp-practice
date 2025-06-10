def solution(a,b,n,arr):
    t=0
    c=b
    i=0
    while c>0 and i<n:
        t+=1
        if c==1:
            taken = False
            while i<n and c+arr[i]<a:
                taken = True
                c+=arr[i]
                i+=1
            if not taken:
                c=a
                i+=1
        else:
            t=t+(c-1)-1
            c=2
        c-=1
    return t+c
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        a,b,n = map(int,lines[i].split())
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(a,b,n,arr))
        i += 2

if __name__ == "__main__":
    main()