from collections import Counter

def solution(s):
    return "CHAT WITH HER!" if len(set(s))%2==0 else "IGNORE HIM!"
            

def main():
    import sys
    input = sys.stdin.read
    s = input().split()

    result = solution(s[0])
    print(result)

if __name__ == "__main__":
    main()