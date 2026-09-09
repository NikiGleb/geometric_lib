def perimeter(a: float, b: float, c: float) -> float:
    return a + b 

def square(a: float, b: float, c: float) -> float:
    p = perimeter(a, b, c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
