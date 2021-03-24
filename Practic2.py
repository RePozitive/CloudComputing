def ValueLine(list, limit_value=3, array_value=[], final_array=[]):
    if len(list) == 0:
        return 0
    for i in list:
        array_value.append([i, len(i)])
    for j in array_value:
        if j[1] >= limit_value:
            final_array.append(j)
    return final_array

array = ["aa", "bbbb", "c", "ffffff", "t", "wwwwwwww"]      #[['bbbb', 4], ['ffffff', 6], ['wwwwwwww', 8]]
array2 = []                                                 # 0
print(ValueLine(array))