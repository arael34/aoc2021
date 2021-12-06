def countIncreases(arr):
    count = 0;
    for i in range (1, len(arr)):
        if arr[i - 1] < arr [i]:
            count += 1
    return count
def main():
    inputL = '''\
100
'''
    arr = [int(line) for line in inputL.splitlines()]
    print(countIncreases(arr))
if __name__ == "__main__":
    main()