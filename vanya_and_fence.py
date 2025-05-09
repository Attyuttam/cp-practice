from collections import Counter

def solution(n, h, arr):
    w = 0
    for i in arr:
        if i <= h:
            w+=1
        else:
            w+=2
    return w
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    h = int(data[1])
    arr = list(map(int, data[2:]))

    result = solution(n,h, arr)
    print(result)

if __name__ == "__main__":
    main()
