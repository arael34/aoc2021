def find_least_distance(arr):
    largest = 0
    zero_sum = 0
    top_sum = 0
    for num in arr:
        if num <= largest: continue
        largest = num
    for num in arr:
        top_sum += largest - num
        zero_sum += num
    temp = (top_sum + zero_sum) // 4 if zero_sum < top_sum else (top_sum + zero_sum) * 3 // 4
    return 1

def main():
    input = '''\
16,1,2,0,4,2,7,1,2,14
'''
    arr = [int(x) for x in input.split(",")]
    print(find_least_distance(arr))

if __name__ == "__main__":
    main()