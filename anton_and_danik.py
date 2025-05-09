from collections import Counter

def solution(n, s):
    a = 0
    d = 0
    for ch in s:
        if ch == "A":
            a+=1
        else:
            d+=1
    return "Anton" if a>d else "Danik" if d>a else "Friendship"
            
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    s = data[1]
    
    result = solution(n,s)
    print(result)

if __name__ == "__main__":
    main()
