def climbStairs(n):
        if n == 1:
            return 1
        elif n==2:
            return 2
        
        first =1 
        second = 2
        for i in range(3,n+1):
            next = first + second
            first = second
            second = next
            return second
        
            return subP1 + subP2
        
        
print(climbStairs(5))



# n=2 2
# n=3 3
# n=4 5
# n=5 8