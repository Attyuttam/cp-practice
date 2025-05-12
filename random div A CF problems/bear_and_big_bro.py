from collections import Counter

def solution(l,b):
    c = 0
    while l<=b :
        c+=1
        l = l*3
        b = b*2
    return c
            
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    l = int(data[0])
    b = int(data[1])
    
    result = solution(l,b)
    print(result)

if __name__ == "__main__":
    main()
