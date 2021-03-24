def FunctionSum(list, value=0):
    if len(list) == value:
        return 0
    else:
        return sum(list)

array = [1, 2, 3, 4, 5]     # 15
array2 = [5, -3, 4, -10]    # -4
print(FunctionSum(array2))
