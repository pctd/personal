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
       