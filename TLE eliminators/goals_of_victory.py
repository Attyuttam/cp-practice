def solution(n,arr):
    return -1 * sum(arr)
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n,arr))
        i += 2

if __name__ == "__main__":
    main()