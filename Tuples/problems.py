# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.

# Example

# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24



def sum_product(input_tuple):
    # TODO
    sum =0
    product =1

    for num in t:
        sum += num
        product *= num
    
    return sum, product


# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

def tuple_elementwise_sum(tuple1, tuple2):

    return tuple(map(sum, zip(tuple1, tuple2)))


# Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

# Example

# input_tuple = (2, 3, 4)
# value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)  # Expected output: (1, 2, 3, 4)

def insert_value_front(input_tuple, value_to_insert):
    # TODO
    return (value_to_insert), + input_tuple



# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

# Example

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

def get_diagonal(tup):
    # TODO
    for i,j in range(len(tup)):
        if tup[i][j] == tup[j][i]:
            return f"the {element} is found at {i} index"
    return 'Elemenr not found'


output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)
