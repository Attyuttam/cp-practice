from collections import Counter

def solution(arr):
    c = 1
    last = str(1-int(arr[0][0]))
    for v in arr:
        if last==v[0]:
            c+=1
            last = v[1]
    return c
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().splitlines()

    n = int(lines[0])
    arr = []
    
    for i in range(1,n+1):
        arr.append(lines[i])
    result = solution(arr)
    print(result)

if __name__ == "__main__":
    main()