from math import sqrt

def euclidean_distance(a: list[float], b: list[float]):
  return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# [x1,y1] [x2,y2]
result = euclidean_distance([2,3], [10,8])

print(result)