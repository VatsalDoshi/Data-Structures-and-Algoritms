def first_second(my_list):
    # TODO
    my_list.sort(reverse = True)
    return my_list[0] , my_list[1]

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87