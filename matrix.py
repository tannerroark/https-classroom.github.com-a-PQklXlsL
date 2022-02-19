import math


class Matrix:
    def __init__(self, array):
        #self.array = LISTOFLIST
        self.array = array
        self.cols = len(self.array[0])
        self.rows = len(array)
        self.shape = (self.cols, self.rows)
        self.size = (self.cols * self.rows)

        for i in self.array:
            len_array = len(i)
            if len_array == self.cols:
                continue
            else:
                raise ValueError("rows dimensions are inconsistent")

    def __repr__(self):
        matrix_s = ""
        for j in range(self.rows):
            matrix_s += "|"
            for k in range(self.cols):
                matrix_s += (" %5.2f" %(self.array[j][k]))
            matrix_s += "  |\n"
        return matrix_s

    def __add__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("dimensions should be the same size")
        else:
            matadd = []
            for j in range(self.rows):
                matadd.append([])
                for k in range(self.cols):
                    matadd[j].append(self.array[j][k] + other.array[j][k])
            return Matrix(matadd)

    def __sub__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("dimensions should be the same size")
        else:
            matsub = []
            for j in range(self.rows):
                matsub.append([])
                for k in range(self.cols):
                    matsub[j].append(self.array[j][k] - other.array[j][k])
            return Matrix(matsub)

    def __mul__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("dimension mismatch! matrices should be the same size")
        else:
            mat_mul = []
            for j in range(self.rows):
                mat_mul.append([])
                for k in range(self.cols):
                    mat_mul[j].append(self.array[j][k] * other.array[j][k])
            return Matrix(mat_mul)

    def __matmul__(self, other):
        if len(self.array[0]) != len(other.array):
            raise ValueError("inner dimension should be the same size")
        else:
            A = self.array
            B = other.array
            C = []
            for x in range(len(A)):
                c = []
                for y in range(len(B[0])):
                    product = 0
                    for z in range(len(A[x])):
                        product += A[x][z]*B[z][y]
                    c.append(product)
                C.append(c)
        return Matrix(C)

    def trace(self):
        trace = 0
        if self.cols != self.rows:
            raise ValueError("matrix should be square")
        else:
            for j in range(self.cols):
                trace += self.array[j][j]
            return (trace)

    def norm(self):
        v_norm = 0
        vector = 0
        if self.cols == 1:
            for j in range(self.rows):
                vector += ((self.array[j][0])**2)
            v_norm += math.sqrt(vector)
            return(v_norm)
        if self.rows == 1:
            for k in range(self.cols):
                vector += ((self.array[0][k]) ** 2)
            v_norm += math.sqrt(vector)
            return(v_norm)
        else:
            raise ValueError("matrix should be 1D")

    def reshape(self, new_rows, new_cols):
        if self.cols*self.rows != new_rows*new_cols:
            raise(ValueError("Matrix size should not change through reshaping"))
        else:
            temp = []
            for i in range(self.rows):
                for j in range(self.cols):
                    temp.append(self.array[i][j])
            count = 0
            new_array = []
            for m in range(new_rows):
                new_array.append([])
                for n in range(new_cols):
                    new_array[m].append(temp[count])
                    count += 1
            self.array = new_array
            self.rows = new_cols
            self.cols = new_cols
            self.shape = (new_rows, new_cols)
            self.size = new_cols*new_rows


#Matrix_A = Matrix([[1, 2, 3], [3, 4, 5], [1, 2, 3]])
#Matrix_D = Matrix([[6, 2, 3], [7, 4, 5], [2, 3, 5]])
#Matrix_E = [1, 2, 3, 4, 5, 6]
#C = Matrix_A + Matrix_B
#Z = Matrix_A - Matrix_B
#Y = Matrix_A * Matrix_B
#X = Matrix_A @ Matrix_B
#print(C)
#print(Z)
#print(Y)
#print(X)
#print(Matrix_A.trace())
#print(Matrix_E.v_norm())
#print(Matrix_A)
#Matrix_E.reshape()
#print(Matrix_A)
#print(Matrix_B)
#print(Matrix_E)


if __name__ == "__main__":
    print()
