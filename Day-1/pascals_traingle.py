import math

def nCr(n,r):
    res = 1

    # Calculating nCr:
    for i in range(r):
        res = res * (n-i)
        res = res // (i +1)

    return res

def pascaltriange(r,c):
    element = nCr(r-1,c-1)
    return element

if __name__ == "__main__":
    r = 5
    c = 3
    element = pascaltriange(r,c)
    print(f"The element at position (r,c) is : {element}")