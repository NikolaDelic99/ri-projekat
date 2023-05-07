import math
from itertools import permutations



def bruteForce(graf, permutation):

  visited = [False for i in range(len(graf))]
  visited[0] = True

  time = 0

  for _ in range(len(graf)-1):
    temp_visited = [i for i in range(len(visited)) if visited[i] == True]

    for j in temp_visited:
      for p in permutation:
        if p in graf[j] and not visited[p]:
          visited[p] = True
          break
        
    time += 1
    if all(visited):
        break

  return time

if __name__ == '__main__':

  fileName = 'graf.txt'
  with open(fileName) as f:
    lines = f.readlines()

  n = int(lines[0])
  graf = [[] for i in range(n)]

  

  i = 1
  while i < len(lines):
    x, y = lines[i].split(" ")
    graf[int(x)].append(int(y))
    graf[int(y)].append(int(x))
    i += 1

  list_permutations = list(permutations(range(1, n)))

  rez = float('inf')

  
        
  i = 0
  while i < len(list_permutations):
    permutation = list_permutations[i]
    print(f'permutation: {permutation}')
    temp_rez = bruteForce(graf, permutation)
    if (temp_rez < rez):
        rez = temp_rez
    i += 1


  
  print(f'Time: {rez} ')
