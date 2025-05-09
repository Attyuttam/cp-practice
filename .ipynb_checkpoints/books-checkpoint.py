def solution(n, t, times):
   print(n)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    t = int(data[1])
    times = list(map(int, data[2:]))

    result = solution(n, t, times)
    print(result)

if __name__ == "__main__":
    main()
