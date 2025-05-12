def solution(n, arr):
    n1 = 0
    m1 = 0
    for v in arr:
        if v == -1:
            if n1 > 0:
                n1 -= 1
            else:
                m1 += 1
        else:
            n1 += v
    return m1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    result = solution(n, arr)
    print(result)

if __name__ == "__main__":
    main()
