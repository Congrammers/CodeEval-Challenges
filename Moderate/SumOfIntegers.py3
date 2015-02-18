import sys

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = list(map(int, line.rstrip().split(',')))
        print(max_subarray(line))
