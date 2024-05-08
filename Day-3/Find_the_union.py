def find_union(arr1, arr2):
    s = set()
    union = []

    for i in arr1:
        s.add(i)
    
    for j in arr2:
        s.add(j)

    for k in s:
        union.append(k)
    return union

arr1 = [100,102,6,8,4,74,7,7,74,9,9,10]
arr2 = [101,5,6,10,9,34,33,1,7,7,100]

Uniion = find_union(arr1,arr2)

print(f"Union of arr1 and 1rr2 is:{Uniion}")