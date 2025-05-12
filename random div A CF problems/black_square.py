def solution(cal, str):
    calsum = 0
    for ch in str:
        calsum+=cal[int(ch)-1]
    return calsum

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    cal = list(map(int,lines[0].split()))
    str = lines[1]

    result = solution(cal, str)
    print(result)

if __name__ == "__main__":
    main()
