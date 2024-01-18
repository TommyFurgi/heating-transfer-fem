import numpy
from scipy import integrate

def e(i, x, h):
    if (x < i * h):
        f = 1/h * x - i + 1
    else:
        f = (-1) * 1/h * x + i + 1

    return max(0, f)

def e_prim(i, x, h):
    if (x < (i - 1) * h) or (x > (i + 1) * h):
        return 0
    elif (x < i * h):
        return 1/h
    else:
        return (-1) * 1/h

def k(x):  
    if x <= 1:
        return 1
    else:
        return 2 * x


def B(i, j, l, r, h):
    return integrate.quad(lambda x: e_prim(i, x, h) * e_prim(j, x, h) * k(x), l, r)[0] - e(i, 0, h) * e(j, 0, h)

def L(i, l, r, h):
    return integrate.quad(lambda x: 100 * x * e(i, x, h), l, r)[0] - e(i, 0, h) * 20

def MatrixA(n, h):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if (abs(i - j) > 1): # always equals 0
                row.append(0)
                continue
            if (abs(i - j) == 1):
                l = max(0, min(i, j) * h)
                r = min(2, max(i, j) * h)   
            else:
                l = max(0, (i - 1) * h)
                r = min(2, (i + 1) * h)   

            row.append(B(j, i, l, r, h))
        matrix.append(row)
    return matrix
            

def MatrixB(n, h):
    matrix = []
    for i in range(n):
        l = max(0, (i - 1) * h)
        r = min(2, (i + 1) * h)
    
        matrix.append(L(i, l, r, h))
    return matrix


def solve(n):
    h = 2 / n

    a = numpy.array(MatrixA(n, h))
    b = numpy.array(MatrixB(n, h))

    x = [h * i for i in range(n + 1)]
    y = numpy.append(numpy.linalg.solve(a, b), 0)
    
    return (x, y)
