def solution(a,b,c):
    if c%2 == 0:
        if a > b:
            return "First"
        else:
            return "Second"
    else:
        if a >= b:
            return "First"
        else:
            return "Second"
        
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    for i in range(1,t+1):
        a,b,c = lines[i].split()
        print(solution(int(a),int(b),int(c)))

if __name__ == "__main__":
    main()