class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0]) if self.rows > 0 else 0

    def __add__(self, other):
        new = []
        if not isinstance(other, Matrix):
            raise TypeError("Можно складывать только матрицы")
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                new.append(row)
        else:
            raise ValueError("Матрицы должны быть одинакового размера")
        return Matrix(new)

    @property
    def T(self):
        return self.transpose()

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Можно умножать только на другую матрицу")
        if self.cols != other.rows:
            if self.rows == other.rows and self.cols == other.cols:
                other = other.T
            else:
                raise ValueError(f"Несовместные размерности: {self.cols} != {other.rows}")
        new = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.matrix[i][k] * other.matrix[k][j]
                new[i][j] = total
        return Matrix(new)

    def __rmul__(self, other):
        new = []
        if isinstance(other, int):
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] * other)
                new.append(row)
        else:
            raise TypeError("Число должно быть int")
        return Matrix(new)

    def __iter__(self):
        for i in range(self.rows):
            for j in range(self.cols):
                yield self.matrix[i][j]

    def __array__(self):
        return list(*self)

    def __len__(self):
        return self.cols * self.rows

    def __repr__(self):
        matrix_str = '\n'.join([str(row) for row in self.matrix])
        return f"Matrix[\n{matrix_str}\n]"

    def transpose(self):
        new = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                new[j][i] = self.matrix[i][j]
        return Matrix(new)

