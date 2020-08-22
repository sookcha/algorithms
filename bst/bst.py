class Node():
    left = None
    right = None
    
    def __init__(data):
        self.data = data

class Tree():
    root = None

    def insert(data):
        if (root == None):
            d = Node(data)
            self.root = d

       current = root
       while (root.left == None or root.right == None):
           if (root.data > data):
               current = root.left
           else:
               current = root.right

       if (current.data > data):
           current.left = Node(data)
       else:
           current.right = Node(data)
   
   """
   1. 노드의 오른쪽 부트리가 존재할 경우, 오른쪽 부트리의 최솟값
   2. 오른쪽 부트리가 없을 경우, 해당 노드에서 왼쪽으로 올라가다가 처음 오른쪽 간선이 생겨서 올라간 node
   3. 위 두 가지 경우에 값이 없는 경우, successor  존재하지 않음(=트리의 최댓값)
   """
   def successor():
       pass

    """
    1. 자식노드가 없는 경우: 그냥 삭제
    2. 자식노드가 1개인 경우: linked list 삭제하듯 삭제
    3. 자식노드가 2개인 경우: 제거할 데이터에 successor로 대치
    """
    def delete():
        pass

    def search(data):
        if (root == None or root.data == data):
            return data

       current = self.root
       
       while (current != None and data != current.data):
          if (data > current.data):
              current = current.right
          else:
              current = current.left

          return current.data

      return None

if __name__ == "__main__":
    pass
