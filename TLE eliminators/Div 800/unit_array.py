def solution(n,arr):
    np = 0
    nn = 0
    for v in arr:
        if v == 1:
            np+=1
        else:
            nn+=1
    if np == n:
        return 0
    if np > nn:
        if nn%2 == 0:
            return 0
        return 1
    else:
        extra = nn-np
        if extra == 0:
            if nn == np:
              if nn%2 == 0:
                  return 0
              return 1
            elif nn == 2 or nn == 3:
                return nn
            else:
                if nn%2 == 0:
                    return nn//2
                else:
                    if (nn//2) %2 == 0:
                        return (nn//2) + 1
                    return (nn//2) + 2
        else:
            toMakeEq = (extra//2) if extra%2==0 else (extra//2 + 1)
            remNeg = nn - toMakeEq
            if remNeg%2 == 0:
                return toMakeEq
            return toMakeEq + 1
def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i].strip())
        arr = [int(c) for c in lines[i+1].split()]
        print(solution(n,arr))
        i+=2

if __name__ == "__main__":
    main()