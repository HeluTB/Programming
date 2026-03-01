import os
def countingSort(arr):
    # Write your code here
    freq = [0] * 100
    x = len(arr)
    for i in range(x):
        freq[arr[i]] += 1
    return freq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
