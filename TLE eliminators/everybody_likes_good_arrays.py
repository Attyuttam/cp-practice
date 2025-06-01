def solution(n,arr):
    num = 0
    even = arr[0]%2==0
    count = 1
    for i in range(1,n):
        if arr[i]%2==0 and even:
            count+=1
        elif arr[i]%2!=0 and not even:
            count+=1
        else:
            num+=(count-1)
            count = 1
            even = arr[i]%2==0
    if count > 1:
        num+=count-1
    return num
    
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = list(map(int, lines[i+1].split()))
        print(solution(n,arr))
        i+=2

if __name__ == "__main__":
    main()