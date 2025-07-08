import math
from typing import Union
from maths.matrix import Matrix

class Vector3D:
    def __init__(self, x: int | float = 0, y: int | float = 0, z: int | float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return F"<Vector3D: {self.x}, {self.y}, {self.z}>"

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    __rmul__ = __mul__

    def __mul__(self, other: Union['Vector3D', int, float]) -> Union['Vector3D', int, float]:
        if isinstance(other, (int, float)):
            return Vector3D(x=self.x * other, y=self.y * other, z=self.z * other)
        if isinstance(other, Vector3D):
            return self.dot(other)
        raise TypeError("Only Vector3d, int, float")

    def __round__(self, n: int = 0) -> 'Vector3D':
        return Vector3D(
            round(self.x, n),
            round(self.y, n),
            round(self.z, n)
        )

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __matmul__(self, other: Matrix) -> 'Vector3D':
        result = other * self.to_matrix()
        if len(result) != 3:
            raise ValueError("неверное число координат")
        x, y, z, = result
        return Vector3D(x=x, y=y, z=z)


    def dot(self, other: 'Vector3D') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(
            x=self.y * other.z - self.z * other.y,
            y=self.z * other.x - self.x * other.z,
            z=self.x * other.y - self.y * other.x
        )

    @property
    def length(self) -> int | float:
        return math.sqrt(self.x * self.x +
                         self.y * self.y +
                         self.z * self.z)

    def normalize(self) -> 'Vector3D':
        if self.length == 0:
            raise ZeroDivisionError("на ноль делить нельзя")
        return Vector3D(self.x / self.length, self.y / self.length, self.z / self.length)

    def projection(self, other: 'Vector3D') -> 'Vector3D':
        return self.dot(other.normalize()) * other.normalize()

    def rotateX(self, angle: int | float) -> 'Vector3D':
        angle = math.radians(angle)
        return Vector3D(x=self.x,
                        y=self.y * math.cos(angle) - self.z * math.sin(angle),
                        z=self.y * math.sin(angle) + self.z * math.cos(angle))
    def rotateY(self, angle: int | float) -> 'Vector3D':
        angle = math.radians(angle)
        return Vector3D(x=self.x * math.cos(angle) + self.z * math.sin(angle),
                        y=self.y,
                        z=-self.x * math.sin(angle) + self.z * math.cos(angle))

    def rotateZ(self, angle: int | float) -> 'Vector3D':
        angle = math.radians(angle)
        return Vector3D(x=self.x * math.cos(angle) - self.y * math.sin(angle),
                        y=self.x * math.sin(angle) + self.y * math.cos(angle),
                        z=self.z)

    def rounded(self, n: int = 10) -> 'Vector3D':
        return Vector3D(
            round(self.x, n),
            round(self.y, n),
            round(self.z, n)
        )

    def rotate_axis(self, axis: 'Vector3D', angle: int | float) -> 'Vector3D':
        angle = math.radians(angle)
        if not math.isclose(axis.length, 1.0, abs_tol=1e-6):
            axis = axis.normalize()
        result = self * math.cos(angle) + axis.cross(self) * math.sin(angle) + axis * self.dot(axis) * (1-math.cos(angle))
        return result

    def to_matrix(self) -> Matrix:
        return Matrix([[self.x], [self.y], [self.z]])
