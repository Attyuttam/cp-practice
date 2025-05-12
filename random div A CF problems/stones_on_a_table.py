from collections import Counter

def solution(n, str):
    c = 0
    i = 0
    j = 1
    
    while j < n and i <= j:
        if str[i] == str[j]:
            c += 1
            j += 1
        else:
            i = j
            j += 1
    return c  

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    str = data[1]

    result = solution(n, str)
    print(result)
    
if __name__ == "__main__":
    main()
