#!/bin/python3

import math
import os
import random
import re
import sys

"""
맨 처음 배열을 나눈 다음, 좌 우 배열을 다시 피봇 기준으로 좌 우로 나누는 과정을 반복.
배열 length가 1이 된 시점에 정렬이 완료된 것으로 판단.
여기서는 재귀를 사용하였음.
"""
def quickSort(arr):
    if len(arr) > 0:
        p = 0
        pivot = arr[p]
        left = list(filter(lambda x: x < pivot, arr))
        right = list(filter(lambda x: x > pivot, arr))

        sorted_left = quickSort(left)
        sorted_right = quickSort(right)
        
        sorted_left.append(pivot)
        result = (sorted_left + sorted_right)

        return result
    else:
        return arr

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    print(result)
