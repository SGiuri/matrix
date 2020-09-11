class Matrix:
    def __init__(self, matrix_string):
        # splitting each line
        self.matrix_string = matrix_string.strip().split("\n")
        pass

    def row(self, index):

        # splitting
        return [int(j) for j in self.matrix_string[index-1].split()]


    def column(self, index):
        my_column = []
        for row_unsplitted in self.matrix_string:
            my_column.append(int(row_unsplitted.split()[index-1]))
        return my_column
