def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(liste))


def reverse_list(lst):
    if not lst: # liste boş ise
        return []
    if isinstance(lst[0], list): # eğer listenin ilk elemanı bir alt liste ise
        return [reverse_list(lst[0])] + reverse_list(lst[1:])
    else:
        return [lst[0]] + reverse_list(lst[1:])
    
liste2=[[1, 2], [3, 4], [5, 6, 7]]
reverse_list(liste2)