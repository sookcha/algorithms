arr = []

def insert(arr, data):
    arr.append(data)
    i = len(arr) - 1

    if (len(arr) < 1):
        return arr

    parent = arr[(i-1)//2]
    while (arr[(i-1)//2] < data and i != 0):
        parent_data = parent
        arr[(i-1)//2] = data
        arr[i] = parent_data

        i = (i-1)//2

    return arr

def sort(arr):
    """
    루트 노드 가져오고 삭제 후
    모든 노드가 텅텅 될 때까지 max_heapify 호출
    """
    result = []
    
    while len(arr) != 0:
        result = [arr.pop(0)] + result
        if(len(arr) == 0):
            break
    
        last_index = len(arr) - 1
        arr = [arr.pop()] + arr
        
        max_heapify(arr, 0)

    return result


"""
부모는 (i-1)/2
자식은 2i+1, 2i+2
"""
def max_heapify(arr, i):
    current = arr[i]
    try:
        child_1 = arr[(2*i)+1]
    except:
        child_1 = 0

    try:
        child_2 = arr[(2*i)+2]
    except:
        child_2 = 0

    if (child_1 < current and child_2 < current):
        return

    """
    child_1과 child_2 사이에 더 큰값을 current와 바꾼 후,
    바뀐 current 자리에서 max_heapify 호출
    """
    if (child_1 > child_2):
        addr = (2*i)+1
    else:
        addr = (2*i)+2

    temp = arr[i]
    arr[i] = arr[addr]
    arr[addr] = temp

    i = addr
    
    max_heapify(arr, i)

    return arr

if __name__ == "__main__":
    arr = insert(arr, 1)
    arr = insert(arr, 3)
    arr = insert(arr, 4)
    arr = insert(arr, 2)
    print(arr)
    print(sort(arr))
