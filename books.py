def solution(n, t, times):
    i,j = 0,0
    ct = 0
    maxbooks = 0
    while i<=j and j<n:
        if ct+times[j] <= t:
            ct+=times[j]
            maxbooks = max(j-i+1,maxbooks)
            j+=1
        else:
            if i == j:
                i+=1
                j+=1
            else:
                ct-=times[i]
                i+=1
    return maxbooks

def main():
    import sys
    input = sys.stdin.read

    n = 7
    t = 13
    times = [6,8,14,9,4,11,10]

    result = solution(n, t, times)
    print(result)

if __name__ == "__main__":
    main()
