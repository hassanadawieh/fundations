

def sum_arr(arr):
    total = 0  # 1 Primitive operations

    for el in arr: # 4 Primitive operations
        total += el

    return total # 1 Primitive operations

# = 6 operations (input of size = 4)
# = 12 operations (input of size = 10)
# = 1002 operations (input of size = 1000)

# N -> Running time linear to N

print(sum_arr([2,3,8,9]))    

#input -> [1,2,3][1,2,3]
#output -> [1,2,3,2,,4,6,3,6,9]

def permutation(arr1,arr2) -> [int]:
    res=[] # 1 operation

    for el1 in arr1:# N operations
        for el2 in arr2: # N operations
            res.append(el1 * el2)

    return res        

# best case
# average case
# worst case

