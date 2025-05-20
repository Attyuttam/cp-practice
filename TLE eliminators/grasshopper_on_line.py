def solution(x,k):
    if x%k!=0:
        print(1)
        print(x)
        return
    v = x//k
    if v%k==0:
        print(2)
        print(v-1,x-v+1)
    else:
        print(2)
        print(v,x-v)
    

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        x,k = map(int, lines[i].split())
        solution(x,k)
        i+=1

if __name__ == "__main__":
    main()