def solution(n,k,x):
    if k == 1 and x == 1:
        print("NO")
        return
    if x!=1:
        print("YES")
        arr = [1 for _ in range(n)]
        print(len(arr))
        print(' '.join(map(str,arr)))
        return
        
    if k==2 and n%2!=0:
        print("NO")
        return
            
    res = []
    temp = n
    if temp%2 != 0:
        res.append(3)
        temp-=3
        
    for i in range(temp//2):
        res.append(2)
    
    if sum(res) == n:
        print("YES")
        print(len(res))
        print(' '.join(map(str,res)))
        return
    print("NO")

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n,k,x = map(int, lines[i].split())
        solution(n,k,x)
        i+=1

if __name__ == "__main__":
    main()