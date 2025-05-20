from io import StringIO
import sys

# Sample test input (as you'd give to stdin)
# Example: 2 test cases
test_input = """2
3
123
4
1357
"""

# Backup original stdin
original_stdin = sys.stdin

# Replace stdin with test_input
sys.stdin = StringIO(test_input)

# Original code (unchanged)
def solution(n, arr):
    i = 1
    sum = 0
    while i < n:
        sum += arr[i] - arr[i-1]
        i += 1
    if sum > 0:
        return "YES"
    return "NO"

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().splitlines()

    t = int(lines[0])
    
    i = 1
    for _ in range(t):
        n = int(lines[i])
        arr = [int(c) for c in lines[i+1]]
        print(solution(n, arr))
        i += 2

if __name__ == "__main__":
    main()

# Restore original stdin (optional in Jupyter, but good practice)
sys.stdin = original_stdin
