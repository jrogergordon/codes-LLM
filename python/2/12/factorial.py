def factorial(n):
    memo = {0: 1, 1: 1}  # initialize memoization dictionary
    def recursive_factorial(n):
        if n in memo:
            return memo[n]
        else:
            result = n * recursive_factorial(n-1)
            memo[n] = result
            return result
    return recursive_factorial(n)
    
ans = factorial(9)
print(ans)