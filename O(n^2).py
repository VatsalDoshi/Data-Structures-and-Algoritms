def print_items(n):
    for i in range(n): # 1 loop so 0(n)
        for j in range(n):  # 1 loop so 0(n)
            print(i,j)
                            # total n*n = n^2
                            #even if 3 loops n*n*n = n^3, we write the complexity as O(n^2)
print_items(100)