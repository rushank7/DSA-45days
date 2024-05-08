def get_single_element(arr):
    x0rr = 0
    for num in arr:
        xorr ^= num
    return xorr

def main():
    arr = [4,1,2,1,2]
    anwser = get_single_element(arr)
    print("The single element is:", anwser)

if __name__ == "__main__":
    main()