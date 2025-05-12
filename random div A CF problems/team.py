from collections import Counter

def solution(n,mat):
    count = 0
    for i in range(n):
        p = mat[i][0]
        v = mat[i][1]
        t = mat[i][2]
        
        if p+v+t >= 2:
            count+=1
            
    return count
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().splitlines()

    n = int(lines[0])
    matrix = [list(map(int, line.split())) for line in lines[1:n+1]]

    result = solution(n, matrix)
    print(result)

if __name__ == "__main__":
    main()