from collections import Counter

def solution(n, arr):
    arr.sort()
    return ' '.join(map(str, arr))
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = solution(n,arr)
    print(result)

if __name__ == "__main__":
    main()
