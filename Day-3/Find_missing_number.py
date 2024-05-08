def missingnumber(a,N):
    xor1 = 0
    xor2 = 0

    for i in range(N-1):
        xor2 = xor2 ^a[i]
        xor1 =