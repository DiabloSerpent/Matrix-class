from collections.abc import Sequence
from utilities import Permfind, sgn, mult  # , swap,swapV2


class matrix(Sequence):
    # "inmat" always refers to input matrix

    def __init__(self, inmat):  # initializes base matrix
        if self.isMatrix(inmat):
            self.base = inmat
        else:
            self.base = [[]]
        self.prevmatrix = self.base
        self.determinant = None

    def __iter__(self):  # iterates through each row of matrix
        if not self.isMatrix():
            self.reset()
        self.row = 0
        return self

    def __next__(self):  # changes current row
        self.row += 1
        if self.row + 1 > len(self.base):
            raise StopIteration
        return self.base[self.row]

    def __len__(self):  # returns no. of rows in matrix
        if not self.isMatrix():
            self.reset()
        return len(self.base)

    def __getitem__(self, key):
        if not self.isMatrix():
            self.reset()
        return self.base[key]

    def __repr__(self):
        return repr(self.base)

    # Checks if given object is a matrix, defaults to checking own matrix
    def isMatrix(self, inmat="No matrix given"):
        if inmat == "No matrix given":
            inmat = self.base
        if type(inmat) != list and type(inmat) != matrix:
            return False
        temp = []

        for row in range(len(inmat)):
            temp.append(0)
            for column in inmat[row]:
                if isinstance(column, (int, float, complex)):
                    temp[row] += 1
                else:
                    return False
        av = 0
        for row in temp:
            av += row
        av /= len(temp)

        for row in temp:
            if not av == row:
                return False

        return True

    def reset(self):
        self.base = [[]]
        self.prevmatrix = self.base
        self.determinant = None

    # get row can be done with "self.base[row]"
    def getc(self, column):  # returns copy of given column
        c = []
        for row in self.base:
            c.append(row[column - 1])
        return c  # column returned as list

    # performs elementwise operations
    def elewise(self, inmat, operation):
        newmat = [[operation(self.base, inmat, row, column) for column in range(len(self.base[row]))] for row in
                  range(len(self.base))]
        return newmat

    def __add__(self, other):
        if not self.isMatrix() or not self.isMatrix(other):
            raise TypeError()
        if len(self.base) != len(other.base) or len(self.base[0]) != len(other.base[0]):
            raise TypeError()
        return self.elewise(other, lambda a, b, r, c: a[r][c] + b[r][c])

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        if not self.isMatrix() or not self.isMatrix(other):
            if isinstance(other, (int, float, complex)):
                return self.elewise(other, lambda a, b, r, c: a[r][c] * b)
            raise TypeError()
        if len(self.base) != len(other.base) or len(self.base[0]) != len(other.base[0]):
            raise TypeError()
        return self.elewise(other, lambda a, b, r, c: a[r][c] * b[r][c])

    def __imul__(self, other):
        return self * other

    # changes base matrix
    def tpose(self):  # transposes matrix
        if not self.isMatrix():
            self.reset()
        newmat = list(zip(*self.base))
        for x in range(len(newmat)):
            newmat[x] = list(newmat[x])
        self.base = newmat

    def fprint(self):  # prints each row separately
        for row in self.base:
            print(row)

    def __matmul__(self, inmat):  # matrix multiplication, returns product
        if not self.isMatrix() or not self.isMatrix(inmat):
            raise TypeError('Base matrix or input matrix isn\'t a matrix')
        if not len(inmat) == len(self.base[0]):
            raise TypeError('Matrices can\'t be multiplied')
        newmat = []
        for row in range(len(self.base)):
            newmat.append([])
            for column in range(len(inmat[0])):
                newmat[row].append(0)
                for no in range(len(self.base[0])):
                    newmat[row][column] += self.base[row][no] * inmat[no][column]
        return newmat

    # sets matrix to base * inmat
    def __imatmul__(self, inmat):
        self.base = self.__matmul__(inmat)
        return self

    @property
    def det(self):  # finds determinant of matrix
        if not self.isMatrix():
            self.reset()
        if len(self.base) != len(self.base[0]):
            raise TypeError('can\t determine determinant')
        if self.prevmatrix == self.base and self.determinant != None:
            return self.determinant
        else:
            self.prevmatrix = self.base
        sizer = range(len(self.base))
        det = 0
        for perm in Permfind(sizer):
            terms = [self.base[x][perm[x]] for x in sizer]
            terms.append(sgn(sizer, perm))
            det += mult(terms)
        self.determinant = det
        return det


m = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
f = matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m + f

# swappable = [x for x in range(10)]
# print(swap(swappable, 3, 7))
# print(swapV2(swappable, 3, 7))
