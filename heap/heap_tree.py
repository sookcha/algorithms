import math

"""
(Min) Binary Heap Tree

array로 구현

i-th element의 부모는
floor((i-1)/2)

자식은
(2i+1), (2i+2)
"""
def tree():
  heap_tree = []

  while(True):
    command = input()
    command = command.split(' ')
    order = command[0]

    if order == '1':
      data = command[1]

      heap_tree = insert(heap_tree, int(data))
      continue

    elif order == '2':
      data = command[1]

      heap_tree = delete(heap_tree, index)
      continue

    else:
      print_tree(heap_tree)
      continue

"""
Min heap 삽입
부모가 새로 들어온 데이터 보다 작을때 까지
부모와 자리 교환 계속 반복
"""
def insert(tree, data):
  tree.append(data)

  if (len(tree) != 1):
    data_index = len(tree) - 1
    parent = math.floor((data_index - 1) / 2)

    while (tree[parent] > data):
      parent_data = tree[parent]
      tree[parent] = data
      tree[data_index] = parent_data

      data_index = parent
      parent = math.floor((data_index - 1) / 2)
      
      if (parent < 0):
        break


  return tree

"""
Heap 중에 특정 element 삭제
"""
def delete(tree, index):
  raise NotImplementedError

def print_tree(tree):
  print(tree[0])

if __name__ == "__main__":
  tree()