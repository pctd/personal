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
        self.array = [[default