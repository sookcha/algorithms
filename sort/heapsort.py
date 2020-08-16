arr = []


def sort():
    """
    부모 노드 가져오고 삭제 후
    모든 노드가 텅텅 될 때까지 max_heapify 호출
    """

"""
부모는 (i-1)/2
자식은 2i+1, 2i+2
"""
def max_heapify(i):
    current = arr[i]
    child_1 = arr[2i+1]
    child_2 = arr[2i+2]

    if(not child_1 and not child_2):
        return

    if (child_1 < current and child_2 < current):
        return

    """
    child_1과 child_2 사이에 더 큰값을 current와 바꾼 후,
    바뀐 current 자리에서 max_heapify 호출
    """

