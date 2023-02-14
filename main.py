def removNb(n):
    total = (n * (n + 1)) // 2 # sum of all numbers from 1 to n
    result = []
    for a in range(1, n+1):
        b = (total - a) // (a + 1) # calculate b
        if b <= n and a * b == total - a - b: # check if a and b satisfy the condition
            result.append((a, b))
    return result
