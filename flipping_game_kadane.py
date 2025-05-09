def solution(n, arr):
    total_ones = sum(arr)
    max_diff = current_diff = 0

    for num in arr:
        val = 1 if num == 0 else -1
        current_diff = max(val, current_diff + val)
        max_diff = max(max_diff, current_diff)

    # Handle the case when all elements are 1
    if max_diff == 0:
        return n - 1

    return total_ones + max_diff
            

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
