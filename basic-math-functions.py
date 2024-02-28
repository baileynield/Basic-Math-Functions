def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    return x * x

def add_squares(x: float, y: float) -> float:
    x.squared = square(x)
    y.squared = square(y)
    return add(x_squared, y_squared)
