def findNumber(lanterns):
  total = 0
  cur_arr = []
  for lantern in lanterns:
    cur_arr.append(lantern)
    for day in range(80):
      for i in range(len(cur_arr)):
        if cur_arr[i] > 0:
          cur_arr[i] -= 1
         else:
          cur_arr[i] = 6
          cur_arr.append(8)
    total += len(cur_arr)
  return total
        
def main():
  input = '''\
  
'''
  lanterns = input.split(",")
  print(findNumber(lanterns))
  
if __name__ == "__main__":
  main()
