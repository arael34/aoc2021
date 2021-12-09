'''
def findNumber(lanterns):
  cur_arr = []
  total = 0
  for lantern in lanterns:
    cur_arr = []
    cur_arr.append(lantern)
    for day in range(100):
      for i in range(len(cur_arr)):
        if cur_arr[i] > 0:
          cur_arr[i] -= 1
        else:
          cur_arr[i] = 6
          cur_arr.append(8)
    total += len(cur_arr)
  return total
'''

# another solution might be to find the amount of 1s, 2s, etc and go from there
'''
def findNumber(lanterns):
  arr = []
  new = 0
  for lantern in lanterns:
    for i in range(9):
      if lantern == i:
        arr[i] += 1
  for day in range(80):
    new = arr.pop(0)
    arr[6] += new; arr[8] += new
  return sum(arr)
'''
  # recursion solution
def findNumber(lanterns, daysLeft):
  cur_arr = []
  if (daysLeft <= 100):
    total = 0
    for lantern in lanterns:
      cur_arr = []
      cur_arr.append(lantern)
      for day in range(100):
        for i in range(len(cur_arr)):
          if cur_arr[i] > 0:
            cur_arr[i] -= 1
          else:
            cur_arr[i] = 6
            cur_arr.append(8)
      total += len(cur_arr)
    return total
  else:
    arr = []
    for lantern in lanterns:
      cur_arr = []
      cur_arr.append(lantern)
      for day in range(100):
        for i in range(len(cur_arr)):
          if cur_arr[i] > 0:
            cur_arr[i] -= 1
          else:
            cur_arr[i] = 6
            cur_arr.append(8)
      arr += cur_arr
    return findNumber(arr, daysLeft - 100) #idk if this is right
  
def main():
  input = '''\
3,4,3,1,2
'''
  lanterns = [int(num) for num in input.split(",")]
  print(findNumber(lanterns, 80))
  
if __name__ == "__main__":
  main()
