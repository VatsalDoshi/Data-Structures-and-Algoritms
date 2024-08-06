

# 1+1+1+1+1+1+1 = 7


# Top Down Memoization
# After breaking the problem we start from last
# eg- here in fibonacci, we calculate last value first and go doen

# def fib(n, memo={}):
#     if n <= 2:
#         return 1
#     elif n not in memo:
#         memo[n] = fib(n-1, memo) + fib(n-2, memo)
#         return memo[n]
    
# n=4
# print(fib(n)) 







# Bottom Up with Tabulation
# Avoids recursion 
# We start from the beginning and fill the table as we go down
# eg- here in fibonacci, we calculate first value first and go down

def fib(n):
    fib_table = [0,1]

    for i in range(2, n+1):
        fib_table.append(fib_table[i-1] + fib_table[i-2])
    return fib_table[n -1]

print(fib(6))
    

# How to identify if the problem can be solved with DP
# 1. Problem has overlapping subproblems
# 2. Optimal solution can be constructed from the solutions of its subproblems
# 3. Problem has optimal substructure




