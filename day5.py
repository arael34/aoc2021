def find_points(lines):
  for line in lines:
    nums = line.split("->")
    x1 = nums[0].split(",")[0]
    y1 = nums[0].split(",")[1]
    x2 = nums[1].split(",")[0]
    y2 = nums[1].split(",")[1]
    if (x1 == x2):
      continue
    elif (y1 == y2):
      continue
  
def main():
  inputLines = '''\
  
'''
  lines = [line.replace(" ", "") for line in inputLines.splitlines()]
  print(find_points(lines))
  
if __name__ == "__main__":
  main()
