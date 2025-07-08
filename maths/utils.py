

def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return (abs(a) * abs(b)) // gcd(a,b)


def factorial(n: int) -> int:
    res = 1
    while n != 0:
        res *= n
        n -= 1
    return res

