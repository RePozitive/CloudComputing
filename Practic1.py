def FunctionSum(list, sum=0):
    for i in list:
        sum += i
    return sum

array = [1, 2, 3, 4, 5]     # 15
array2 = [5, -3, 4, -10]    # -4
array3 = []                 # 0
print(FunctionSum(array2))
