def divide(a: int, b: int) -> tuple:
    result = int(a / b)
    rest = a - (result * b)
    return result, rest


a = 19
b = 3
print(divide(a, b))
