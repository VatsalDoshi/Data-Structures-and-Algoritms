def diagonal_sum(matrix):
    # TODO
    right = 0
    left = 0
    for i in range(len(matrix)):
        right += matrix[i][i]
        print(right)
        left += matrix[-i][-i]
        print(left)
    return right , left


myList2D= [[4,2,3],[4,5,6],[7,8,9]] 

print(diagonal_sum(myList2D)) # 15