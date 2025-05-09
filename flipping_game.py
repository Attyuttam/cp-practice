def solution(n, bins):
    l,r = 0,0
    ones = bins.count(1)
    maxones = 0
    
    for l in range(0,n):
        c = ones
        for r in range(l,n):
            if bins[r] == 0:
                c+=1
            else:
                c-=1
            maxones = max(c,maxones)
    return maxones
            

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    bins = list(map(int, data[1:]))

    result = solution(n, bins)
    print(result)

if __name__ == "__main__":
    main()
