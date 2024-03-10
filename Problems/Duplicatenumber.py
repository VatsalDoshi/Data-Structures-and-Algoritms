def remove_duplicates(arr):
    # TODO
    unique_set = set()
    result_list = []

    for num in arr:
        if num not in unique_set:
            unique_set.add(num)
            result_list.append(num)

    return result_list
        
            
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
# Output : [1, 2, 3, 4, 5]