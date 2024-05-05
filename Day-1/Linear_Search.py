def linear_Search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    num = 4
    result = linear_Search(arr,num)
    print(result)