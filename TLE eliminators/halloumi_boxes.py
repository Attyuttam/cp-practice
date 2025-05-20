def solution(n, k, arr):
    i = 1
    flag = False
    while i<len(arr):
        if arr[i] < arr[i-1]:
            flag = True
            break
        i+=1
    if flag == False:
        return "YES"
        
    if n==1 and k==1:
        return "YES"
    if n>1 and k>1:
        return "YES"
    return "NO"
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n, k = map(int, lines[i].split())
        arr = list(map(int, lines[i+1].split()))
        print(solution(n, k, arr))
        i+=2

if __name__ == "__main__":
    main()
