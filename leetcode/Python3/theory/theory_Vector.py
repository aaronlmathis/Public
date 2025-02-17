from __future__ import annotations

class Vector:
    def __init__(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Both x and y must be integers.")
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector")
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector")
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int) -> Vector:
        if not isinstance(scalar, int):
            raise TypeError("Operand must be an integer")
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: int) -> Vector:
        if not isinstance(scalar, int):
            raise TypeError("Operand must be an integer")
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Vector(self.x // scalar, self.y // scalar)  # Use integer division

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"