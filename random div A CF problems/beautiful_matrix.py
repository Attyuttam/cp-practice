from collections import Counter

def solution(mat):
    x,y = 0,0
    for i in range(0,5):
        flag = 0
        for j in range(0,5):
            if mat[i][j] == 1:
                x = i
                y = j
                flag = 1
                break
                
        if flag == 1:
            break
    
    return abs(2-x) + abs(2-y)
                
            
            

def main():
    import sys
    input = sys.stdin.read
    lines = input().splitlines()

    matrix = [list(map(int, line.split())) for line in lines[0:5]]

    result = solution(matrix)
    print(result)

if __name__ == "__main__":
    main()