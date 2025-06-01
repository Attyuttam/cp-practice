def solution(n,arr):
    two_count = 0
    for a in arr:
        if a==2:
            two_count+=1
    
    if two_count==0:
        return 1
    if two_count==1 or two_count%2!=0:
        return -1
    
    req_two_num = two_count//2
    curr_two_num = 0
    
    for i in range(0,n):
        if arr[i] == 2:
            curr_two_num+=1
        if curr_two_num == req_two_num:
            return i+1
        

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