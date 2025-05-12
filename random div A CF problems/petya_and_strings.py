from collections import Counter

def solution(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if s1 < s2:
        return "-1"
    elif s1 > s2:
        return "1"
    return "0"
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().splitlines()

    s1 = lines[0]
    s2 = lines[1]

    result = solution(s1, s2)
    print(result)

if __name__ == "__main__":
    main()