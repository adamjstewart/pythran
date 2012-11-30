#pythran export solve()
def solve():
    '''
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    
    Find the sum of all the even-valued terms in the sequence which do not exceed four million.
    '''
    
    cache = {}
    def fib(n):
        cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fib(n-1) + fib(n-2))
        return cache[n]
    
    n = 0
    i = 0
    while fib(i) <= 4000000:
        if not fib(i) % 2: n = n + fib(i)
        i = i + 1
    
    return n
