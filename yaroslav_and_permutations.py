from collections import Counter

def solution(n, arr):
    if len(arr) == 1:
        return "YES"
    freq = Counter(arr)
    max_count = max(freq.values())
    
    if max_count > (n + 1) // 2:
        return "NO"
    else:
        return "YES"
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = solution(n, arr)
    print(result)

if __name__ == "__main__":
    main()
