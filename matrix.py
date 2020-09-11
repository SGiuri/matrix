class Matrix:
    """
    A class used to represent Matrix

    ...

    Attributes
    ----------
    matrix_string : str
        string with embedded newlines like:

        "9 8 7\n5 3 2\n6 6 7"

    Methods
    -------
    row(index)
        returns the index row
    """

    def __init__(self, matrix_string):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        # splitting the string in double-levelled list of string
        self.matrix_string = [row.split() for row in matrix_string.strip().split("\n")]

    def row(self, index):
        # converting each element of "index"th row to "int" and returning it as list
        return [int(j) for j in self.matrix_string[index - 1]]

    def column(self, index):
        # converting each "index"th element of each row in int and returning as list
        return [int(k[index - 1]) for k in self.matrix_string]
