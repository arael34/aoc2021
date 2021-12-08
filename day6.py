def findNumber(lanterns):
  total = 0
  cur_arr = []
  for lantern in lanterns:
    cur_arr = []
    cur_arr.append(lantern)
    for day in range(200):
      for i in range(len(cur_arr)):
        if cur_arr[i] > 0:
          cur_arr[i] -= 1
        else:
          cur_arr[i] = 6
          cur_arr.append(8)
    total += len(cur_arr)
  return total

  # make new fish with number and spawn day and calculate from there
        
def main():
  input = '''\
3,4,3,1,2
'''
  lanterns = [int(num) for num in input.split(",")]
  print(findNumber(lanterns))
  
if __name__ == "__main__":
  main()
