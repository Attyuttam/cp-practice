from collections import Counter

def solution(s):
    lc, uc = 0,0
    for ch in s:
        if ch.islower():
            lc+=1
        elif ch.isupper():
            uc+=1
    if lc<uc:
        return s.upper()
    return s.lower()
            

def main():
    import sys
    input = sys.stdin.read
    s = input().split()

    result = solution(s[0])
    print(result)

if __name__ == "__main__":
    main()