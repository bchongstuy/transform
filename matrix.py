from math import *
"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    m = new_matrix()
    ident(m)
    arr = [x, y, z]
    for i in range(3):
        set_value(m, i, 3, arr[i])
    # print_matrix(m)
    return m


def make_scale( x, y, z ):
    m = new_matrix()
    arr = [x, y, z, 1]
    for i in range(4):
        set_value(m, i, i, arr[i])
    # print_matrix(m)
    return m

def make_rotX( theta ):
    m = new_matrix()
    ident(m)
    set_value(m, 1, 1, cos(radians(theta)))
    set_value(m, 2, 2, cos(radians(theta)))
    set_value(m, 2, 1, sin(radians(theta)))
    set_value(m, 1, 2, -sin(radians(theta)))
    # print_matrix(m)
    return m

def make_rotY( theta ):
    m = new_matrix()
    ident(m)
    set_value(m, 0, 0, cos(radians(theta)))
    set_value(m, 2, 2, cos(radians(theta)))
    set_value(m, 0, 2, sin(radians(theta)))
    set_value(m, 2, 0, -sin(radians(theta)))
    # print_matrix(m)
    return m

def make_rotZ( theta ):
    m = new_matrix()
    ident(m)
    set_value(m, 0, 0, cos(radians(theta)))
    set_value(m, 1, 1, cos(radians(theta)))
    set_value(m, 1, 0, sin(radians(theta)))
    set_value(m, 0, 1, -sin(radians(theta)))
    # print_matrix(m)
    return m

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


# custom functions
def multiply_add_two_arrays(arr1, arr2):
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum


def get_value(matrix, row, col):
    return matrix[col][row]


def set_value(matrix, row, col, value):
    matrix[col][row] = value


def get_row_count(matrix):
    if (len(matrix) == 0):
        return 0
    return len(matrix[0])


def get_col_count(matrix):
    return len(matrix)


def get_row(matrix, row):
    arr = []
    for i in range(get_col_count(matrix)):
        arr.append(get_value(matrix, row, i))
    return arr


def get_col(matrix, col):
    return matrix[col]