def solution(n,arr):
    return min([abs(c) for c in arr])
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    n = int(lines[0])
    arr = [int(c) for c in lines[1].split()]
    
    res = solution(n,arr)
    print(res)
    
if __name__ == "__main__":
    main()