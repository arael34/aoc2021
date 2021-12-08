import re

def find_line(a, b):
  lolz = []
  if a[0] == a[1] or b[0] == b[1]:
    for xpoint in range(a[0], a[1] + 1):
      for ypoint in range(b[0], b[1] + 1):
        lolz.append([xpoint, ypoint])
    return lolz
  else :
    for i in range(a[1] - a[0]):
      lolz.append([i + a[0], ])
      # range = a[1] - a[0] , increment steps by one and append to arr , make sure line is diagonal
    return lolz
  # MAYBE make this function part of find_points because diagonal lines shouldn't be sorted

def find_points(lines):
  list = []
  intersections = []
  for line in lines:
    nums = re.split('->|,', line)
    x = sorted([int(nums[0]), int(nums[2])])
    y = sorted([int(nums[1]), int(nums[3])])
    for xpoint in range(x[0], x[1] + 1):
      for ypoint in range(y[0], y[1] + 1):
        point = str(xpoint) + " " + str(ypoint)
        if not(point in intersections) and not(point in list):
          list.append(point)
        elif not(point in intersections) and point in list:
          intersections.append(point)
  return len(intersections)
  
def main():
  inputLines = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
  lines = [line.replace(" ", "") for line in inputLines.splitlines()]
  print(find_points(lines))
  
if __name__ == "__main__":
  main()
