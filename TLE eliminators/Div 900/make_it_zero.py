def solution(n,arr):
    if n%2 == 0:
        print(2)
        print(f"1 {n}")
        print(f"1 {n}")
    else:
        print(4)
        print(f"1 {n-1}")
        print(f"1 {n-1}")
        print(f"{n-1} {n}")
        print(f"{n-1} {n}")
       
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1].split()]
        solution(n,arr)
        i += 2

if __name__ == "__main__":
    main()