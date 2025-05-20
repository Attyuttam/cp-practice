def solution(arr):
    points = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'X':
                if i == 0 or j == 0 or i == 9 or j == 9:
                    points+=1
                elif i==1 or j==1 or i==8 or j==8:
                    points+=2
                elif i==2 or j==2 or i==7 or j==7:
                    points+=3
                elif i==3 or j==3 or i==6 or j==6:
                    points+=4
                elif i==4 or j==4 or i==5 or j==5:
                    points+=5
    return points
            
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):        
        arr = []
        for k in range(10):
            arr.append([c for c in lines[i]])
            i+=1
            
        print(solution(arr))

if __name__ == "__main__":
    main()