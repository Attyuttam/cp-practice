def start_and_end_differ(bstr):
    return bstr[0] != bstr[len(bstr)-1]

def solution(n,bstr):
    while len(bstr)>0 and start_and_end_differ(bstr):
        #print(f"before: {bstr}")
        bstr = bstr[1:len(bstr)-1]
        #print(f"after: {bstr}")
        
    return len(bstr)
        

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        bstr = lines[i+1]
        print(solution(n,bstr))
        i+=2

if __name__ == "__main__":
    main()