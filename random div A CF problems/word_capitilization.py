from collections import Counter

def solution(s):
    return s[0].upper()+s[1:]
            

def main():
    import sys
    input = sys.stdin.read
    s = input().split()

    result = solution(s[0])
    print(result)

if __name__ == "__main__":
    main()