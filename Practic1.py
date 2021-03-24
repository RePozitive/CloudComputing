def FunctionSum(list, value=0):
    if len(list) == 0:
        return 0
    else:
        return sum(list)

array = [1, 2, 3, 4, 5]     
array2 = [5, -3, 4, -10]
print(FunctionSum(array2))