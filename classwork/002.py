def search_decl(target, array, i=0, count=0):
    if i >= len(array):
        return count
    tmp = 0
    if isinstance(array[i], list):
        tmp = search_decl(target, array[i], i=0, count=0)
    if array[i] == target:
        count += 1
    return search_decl(target, array, i=i+1, count=count + tmp)