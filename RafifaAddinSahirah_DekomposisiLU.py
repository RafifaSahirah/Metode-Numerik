import numpy as np
import scipy

def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    print("L = ", L)
    print("\nU = ", U,"\n")
    return L, U

def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double);
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
    return y

def back_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double);
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

def lu_solve(A, b):
    "1. Mencari L dan U dengan cara pada fungsi lu(A) diatas"
    L, U = lu(A)
    "2. Mencari y dengan subsitusi L pada Ly=b"
    y = forward_substitution(L, b)
    "3. Mencari x dengan subsitusi y pada Ux=y"
    x = back_substitution(U, y)
    print("Nilai x yang dicari ialah : ")
    for i in range(len(x)):
        print('X%d = %0.2f' % (i, x[i]), end='\t')

if __name__ == "__main__":
    "Syarat : harus double inputnya"
    A = np.array([[1.0, 1.0, 0, 3.0], [2.0, 1.0, -1.0, 1.0], [3.0, -1.0, -1.0, 2.0], [-1.0, 2.0, 3.0, -1.0]])
    b = np.array([4.0, 1.0, -3.0, 4.0])

    lu_solve(A, b)
    """x= np.allclose(lu_solve(A, b), scipy.linalg.solve(A, b))
    print (x)"""




