class Matrix:
    """
    <class Matrix>
    Matrix structure.
    """

    def __init__(self, row: int, column: int, default_value: float = 0):
        """
        <method Matrix.__init__>
        Initialize matrix with given size and default value.

        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a
        Matrix consist of 2 rows and 3 columns
        [1, 1, 1]
        [1, 1, 1]
        """

        self.row, self.column = row, column
        self.array = [[default_value for c in range(column)] for r in range(row)]

    def __str__(self):
        """
        <method Matrix.__str__>
        Return string representation of this matrix.
        """

        # Prefix
        s = "Matrix consist of %d rows and %d columns\n" % (self.row, self.column)

        # Make string identifier
        max_element_length = 0
        for row_vector in self.array:
            for obj in row_vector:
                max_element_length = max(max_element_length, len(str(obj)))
        string_format_identifier = "%%%ds" % (max_element_length,)

        # Make string and return
        def single_line(row_vector):
            nonlocal string_format_identifier
            line = "["
            line += ", ".join(string_format_identifier % (obj,) for obj in row_vector)
            line += "]"
            return line

        s += "\n".join(single_line(row_vector) for row_vector in self.array)
        return s

    def __repr__(self):
        return str(self)

    def validateIndices(self, loc: tuple):
        """
        <method Matrix.validateIndices>
        Check if given indices are valid to pick element from matrix.

        Example:
        >>> a = Matrix(2, 6, 0)
        >>> a.validateIndices((2, 7))
        False
        >>> a.validateIndices((0, 0))
        True
        """
        if not (isinstance(loc, (list, tuple)) and len(loc) == 2):
            return False
        elif not (0 <= loc[0] < self.row and 0 <= loc[1] < self.column):
            return False
        else:
            return True

    def __getitem__(self, loc: tuple):
        """
        <method Matrix.__getitem__>
        Return array[row][column] where loc = (row, column).

        Example:
        >>> a = Matrix(3, 2, 7)
        >>> a[1, 0]
        7
        """
        assert self.validateIndices(loc)
        return self.array[loc[0]][loc[1]]

    def __setitem__(self, loc: tuple, value: float):
        """
        <method Matrix.__setitem__>
        Set array[row][column] = value where loc = (row, column).

        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a[1, 2] = 51
        >>> a
        Matrix consist of 2 rows and 3 columns
        [ 1,  1,  1]
        [ 1,  1, 51]
        """
        assert self.validateIndices(loc)
        self.array[loc[0]][loc[1]] = value

    def __add__(self, another):
        """
        <method Matrix.__add__>
        Return self + another.

        Example:
        >>> a = Matrix(2, 1, -4)
        >>> b = Matrix(2, 1, 3)
        >>> a+b
        Matrix consist of 2 rows and 1 columns
        [-1]
        [-1]
        """

        # Validation
        assert isinstance(another, Matrix)
        assert self.row == another.row and self.column == another.column

        # Add
        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = self[r, c] + another[r, c]
        return result

    def __neg__(self):
        """
        <method Matrix.__neg__>
        Return -self.

        Example:
        >>> a = Matrix(2, 2, 3)
        >>> a[0, 1] = a[1, 0] = -2
        >>> -a
        Matrix consist of 2 rows and 2 columns
        [-3,  2]
        [ 2, -3]
        """

        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = -self[r, c]
        return result

    def __sub__(self, another):
        return self + (-another)

    def __mul__(self, another):
        """
        <method Matrix.__mul__>
        Return self * another.

        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a[0,2] = a[1,2] = 3
        >>> a * -2
        Matrix consist of 2 rows and 3 columns
        [-2, -2, -6]
        [-2, -2, -6]
        """

        if isinstance(another, (int, float)):  # Scalar multiplication
            result = Matrix(self.row, self.column)
            for r in range(self.row):
                for c in range(self.column):
                    result[r, c] = self[r, c] * another
            return result
        elif isinstance(another, Matrix):  # Matrix multiplication
            assert self.column == another.row
            result = Matrix(self.row, another.column)
            for r in range(self.row):
                for c in range(another.column):
                    for i in range(self.column):
                        result[r, c] += self[r, i] * another[i, c]
            return result
        else:
            raise TypeError(
                "Unsupported type given for another ({})".format(type