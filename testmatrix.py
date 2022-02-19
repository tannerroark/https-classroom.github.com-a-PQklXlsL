import random
import unittest

import numpy as np

import matrix


class TestMatrices(unittest.TestCase):

    def test_init(self):
        A, _ = gen_array()
        A.array[0].pop()
        with self.assertRaises(ValueError):
            matrix.Matrix(A.array)

    def test_size(self):
        A, A_np = gen_array()
        assert A.size == A_np.size

    def test_shape(self):
        A, A_np = gen_array()
        assert A.shape == A_np.shape

    def test_add_dimensions(self):
        A, A_np = gen_array()
        m, n = A.shape
        B, B_np = gen_array(m, n - 1)

        with self.assertRaises(ValueError):
            A + B

    def test_add(self):
        A, A_np = gen_array()
        m, n = A.shape
        B, B_np = gen_array(m, n)

        C = A + B
        C_np = A_np + B_np
        C_test = np.array(C.array)

        np.testing.assert_array_equal(C_test, C_np)

    def test_substract_dimensions(self):
        A, _ = gen_array()
        m, n = A.shape
        B, B_np = gen_array(m, n - 1)

        with self.assertRaises(ValueError):
            A - B

    def test_subtract(self):
        A, A_np = gen_array()
        m, n = A.shape
        B, B_np = gen_array(m, n)

        C = A - B
        C_np = A_np - B_np
        C_test = np.array(C.array)

        np.testing.assert_array_equal(C_test, C_np)

    def test_mult_dimensions(self):
        A, _ = gen_array()
        m, n = A.shape
        B, B_np = gen_array(m, n - 1)

        with self.assertRaises(ValueError):
            A * B

    def test_mult(self):
        A, A_np = gen_array()
        m, n = A.shape
        B, B_np = gen_array(m, n)

        C = A * B
        C_np = A_np * B_np
        C_test = np.array(C.array)

        np.testing.assert_array_equal(C_test, C_np)

    def test_mat_mul_dimensions(self):
        A, _ = gen_array(n=4)
        B, _ = gen_array(m=3)

        with self.assertRaises(ValueError):
            A @ B

    def test_mat_mult(self):
        A, A_np = gen_array(n=5)
        m, n = A.shape
        B, B_np = gen_array(m=5)

        C = A @ B
        C_np = A_np @ B_np
        C_test = np.array(C.array)

        np.testing.assert_array_almost_equal(C_test, C_np)

    def test_trace_dimensions(self):
        A, _ = gen_array(m=4, n=3)

        with self.assertRaises(ValueError):
            A.trace()

    def test_trace(self):
        A, A_np = gen_array(m=5, n=5)

        assert A.trace() == np.trace(A_np)

    def test_norm_dimensions(self):
        A, _ = gen_array()

        with self.assertRaises(ValueError):
            A.norm()

    def test_norm(self):
        A, A_np = gen_array(n=1)

        assert abs(A.norm() - np.linalg.norm(A_np)) < 1e-6

    def test_reshape_dimensions(self):
        A, _ = gen_array(m=5, n=4)

        with self.assertRaises(ValueError):
            A.reshape(5, 5)

    def test_reshape(self):
        A, A_np = gen_array(m=5, n=4)

        A.reshape(4, 5)
        A_np = A_np.reshape(4, 5)

        A_test = np.array(A.array)

        np.testing.assert_array_equal(A_test, A_np)


def gen_array(m=None, n=None):
    if m == None:
        m = random.randint(2, 6)
    if n == None:
        n = random.randint(2, 6)

    array = []
    for i in range(m):
        array.append([])
        for j in range(n):
            array[i].append(random.uniform(-10, 10))

    A = matrix.Matrix(array)
    A_np = np.array(array)
    return A, A_np


if __name__ == '__main__':
    unittest.main()





