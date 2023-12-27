def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)

#When we use 2 loops the complexity becomes 0(2n), but we drop the constant wheater it be 2 or 100. The complexity still remains O(n).
