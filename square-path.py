n = int(input("Number: "))

class Node:

  def __init__(self, val, previous, prev):
    self.num = val
    self.prior = previous
    self.prior.append(prev)
    self.cons = []
    for i in range(1, n + 1):
      if (i + val) ** 0.5 % 1 == 0 and indexOf(self.prior, i) == -1 and val != i:
        self.cons.append(i)

  def __str__(self):
    return self.num

  def getPath(self):
    result = ""
    for a in self.prior:
      if a != 0:
        result += str(a) + " "
    return result + str(self.num)


def findNext(nodes):
  if len(nodes) == 0:
    return False

  if len(nodes[0].prior) == n:
    return nodes

  next = []

  for node in nodes:
    for a in node.cons:
      next.append(Node(a, copy(node.prior), node.num))

  return findNext(next)


def indexOf(arr, val):
  for i in range(len(arr)):
    if val == arr[i]:
      return i
  return -1


def copy(arr):
  result = []
  for thing in arr:
    result.append(thing)

  return result


def path(n):
  print("Starting... {}".format(n))
  result = []
  nodes = []

  for i in range(1, n + 1):
    nodes.append(Node(i, [], 0))

  result = findNext(nodes)
  if result != False:
    print(result[0].getPath())
  else:
    print("No path!")
  print()


path(n)
