from collections import Counter

def solution(n,k,s):
    freq = Counter(s)
    odd_occ = 0
    for char, count in freq.items():
        if count%2!=0:
            odd_occ+=1
    return "YES" if odd_occ <= k + 1 else "NO"
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n,k = map(int,lines[i].split())
        s = lines[i+1]
        print(solution(n,k,s))
        i += 2

if __name__ == "__main__":
    main()