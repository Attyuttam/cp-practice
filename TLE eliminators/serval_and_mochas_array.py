from math import gcd

def solution(n,arr):
    for i in range(n-1):
        for j in range(i+1,n):
            if gcd(arr[i],arr[j]) <= 2:
                return "Yes"
                
    return "No"
        

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