
from typing import List

def rewoveduplciates_(arr : List[int]) -> int:
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i +1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = rewoveduplciates_(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")