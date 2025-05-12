def solution(s):
    if len(s) == 1:
        return 0
    i = 1
    sum = 0
    while i<len(s):
        c2 = ord(s[i])-65
        c1 = ord(s[i-1])-65
        
        if c1 > c2:
            t = c1
            c1 = c2
            c2 = t
        #c2 is always greater
        
        if c2 - c1 > 13:
            sum+=(25 - c2 + c1 + 1)
        else:
            sum+=(c2-c1)
        i+=1
    return sum
            
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    s = lines[0]
    s = 'a'+s if s[0] != 'a' else s
    result = solution(s)
    print(result)

if __name__ == "__main__":
    main()