"""
두 array에서 더 작은 값을 tmp array로 옮기고
어느 한 쪽이 없어질 때까지 반복
한 쪽만 완료됐으면 남은 부분은 그대로 옮김
tmp -> original array로 옮김
"""
def merge(arr, arr_1, arr_2):
    tmp = []
    i = 0
    j = 0
    k = 0

    while(i < len(arr_1) and j < len(arr_2)):
        if (arr_1[i] > arr_2[j]):
            tmp.append(arr_2[j])
            j+=1
        else:
            tmp.append(arr_1[i])
            i+=1

    while(i < len(arr_1)):
        tmp.append(arr_1[i])
        i+=1

    while(j < len(arr_2)):
        tmp.append(arr_2[j])
        j+=1

    for index in range(len(tmp)):
        arr[index] = tmp[index]

    return arr

"""
주어진 array를 반띵하고 merge 하는 것 반복
array length가 1이 될 때까지
"""
def divide(arr):
    if len(arr) <= 1:
        return

    half = len(arr) // 2
    arr_1 = arr[:(half)]
    arr_2 = arr[half:len(arr)]

    divide(arr_1)
    divide(arr_2)

    return merge(arr, arr_1, arr_2)

if __name__ == '__main__':
    print(divide([5,3,6,1,2]))
