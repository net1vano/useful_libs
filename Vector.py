class Vector3D:
    def __init__(self, x: int | float = 0, y: int | float = 0, z: int | float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return F"<Vector3D: {self.x}, {self.y}, {self.z}>"

    def __add__(self, other: 'Vector3D'):
        return Vector3D(x=self.x + other.x, y=self.y+other.y, z=self.z+other.y)

    def __sub__(self, other: 'Vector3D'):
        return Vector3D(x=self.x - other.x, y=self.y - other.y, z=self.z - other.y)

    def __rmul__(self, other):
        if not isinstance(other, int | float):
            raise TypeError("Скалярное умножение можно делать только на числа")
        return Vector3D(x=self.x * other, y=self.y * other, z=self.z * other)

    def __mul__(self, other: 'Vector3D'):
        return Vector3D(x=self.x * other.x, y=self.y * other.y, z=self.z * other.y)

