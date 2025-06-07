def solution(a,b,xk,yk,xq,yq):
    kset = []
    qset = []
    
    kset.append((xk+a,yk+b))
    kset.append((xk+a,yk-b))
    kset.append((xk-a,yk+b))
    kset.append((xk-a,yk-b))
    kset.append((xk+b,yk+a))
    kset.append((xk+b,yk-a))
    kset.append((xk-b,yk+a))
    kset.append((xk-b,yk-a))
    
    qset.append((xq+a,yq+b))
    qset.append((xq+a,yq-b))
    qset.append((xq-a,yq+b))
    qset.append((xq-a,yq-b))
    qset.append((xq+b,yq+a))
    qset.append((xq+b,yq-a))
    qset.append((xq-b,yq+a))
    qset.append((xq-b,yq-a))
    
    return len(list(set(kset) & set(qset)))

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        a,b = map(int,lines[i].split())
        xk,yk = map(int, lines[i+1].split())
        xq,yq = map(int, lines[i+2].split())
        print(solution(a,b,xk,yk,xq,yq))
        i += 3

if __name__ == "__main__":
    main()