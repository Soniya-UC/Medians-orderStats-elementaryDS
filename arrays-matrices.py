class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def insert(self, index, value):
        if self.size >= self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[None for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.data[row][col] = value

    def delete(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.data[row][col] = None

    def access(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        return self.data[row][col]

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)

# arrays
if __name__ == "__main__":
    arr = Array(5)
    arr.insert(0, 5)
    arr.insert(1, 10)
    arr.insert(2, 20)
    print("Array:", arr)
    arr.delete(1)
    print("After deletion:", arr)
    print("Access index 1:", arr.access(1))

#matrices
if __name__ == "__main__":
    mat = Matrix(3, 3)
    # Insert elements for row 1 = [1, 2, 3]
    mat.insert(0, 0, 1)
    mat.insert(0, 1, 2)
    mat.insert(0, 2, 3)
    # Insert elements for row 2 = [2, 3, 1]
    mat.insert(1, 0, 2)
    mat.insert(1, 1, 3)
    mat.insert(1, 2, 1)
    # Insert elements for row 3 = [3, 1, 2]
    mat.insert(2, 0, 3)
    mat.insert(2, 1, 1)
    mat.insert(2, 2, 2)
    print("Matrix:\n", mat)
    mat.delete(1, 2)
    print("After deletion:\n", mat)
    print("Access (1, 2):", mat.access(1, 2))