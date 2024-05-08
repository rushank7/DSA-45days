def missingnumber(a,N):
    xor1 = 0
    xor2 = 0

    for i in range(N-1):
        xor2 = xor2 ^ a[i]
        xor1 = xor1 ^ (i+1)

    xor1 = xor1 ^ N

    return xor1 ^ xor2

def main():
    N = 5
    a = [1,2,4,5]
    answer = missingnumber(a,N)
    print("The missing number is", answer)

if __name__ == '__main__':
    main()