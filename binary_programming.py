from cvxopt import matrix
from cvxopt.glpk import ilp
import numpy as np
from utils import *

"""
 Solves the mixed integer linear programming problem

        minimize    c'*x
        subject to  G*x <= h
                    A*x = b
                    x[k] is integer for k in I
                    x[k] is binary for k in B

    ARGUMENTS
    c            nx1 dense 'd' matrix with n>=1

    G            mxn dense or sparse 'd' matrix with m>=1

    h            mx1 dense 'd' matrix

    A            pxn dense or sparse 'd' matrix with p>=0

    b            px1 dense 'd' matrix

    I            set of indices of integer variables

    B            set of indices of binary variables

    status       if status is 'optimal', 'feasible', or 'undefined',
                 a value of x is returned and the status string
                 gives the status of x.  Other possible values of              status are:  'invalid formulation',
                 'infeasible problem', 'LP relaxation is primal
                 infeasible', 'LP relaxation is dual infeasible',
                 'unknown'.

    x            a (sub-)optimal solution if status is 'optimal',
                 'feasible', or 'undefined'.  None otherwise

"""


def indicator_to_arrangment(indicator_matrix):
    neighbors = {}
    for i in range(0, indicator_matrix.shape[0]):
        for j in range(0, indicator_matrix.shape[1]):
            if indicator_matrix[i,j]==1:
                neighbors[concat_str(i,j)]=True
                neighbors[concat_str(j,i)]=True
    return neighbors


def create_matrix(x, num_images):
    """
    x: is a vector which has n^2-n num_elements (All the elmenst of a nxn matrix other than diagonal elements)
    """
    indicator_matrix = np.zeros((num_images, num_images))
    itr = 0
    for i in range(num_images):
        for j in range(num_images):
            if i!=j:
                indicator_matrix[i,j] =x[itr]
                itr+=1
    return indicator_matrix

def create_transpose_sum_constraint(num_images):
    num_elements = num_images*num_images - num_images
    transpose_constraint = np.zeros((int(num_elements/2), num_elements))
    # step = num_images-1
    reduce_step_flag = False
    j=0
    itr = 0
    for i in range(0, num_elements):
        # print(i)
        if i%(num_images-1)==0:
            step = num_images-1
            reduce_step_flag = True
        # if j<num_elements
        if np.sum(transpose_constraint[:,j])==0:
            transpose_constraint[itr, j]=1
            transpose_constraint[itr, j+step]=1
            itr+=1
            # print(transpose_constraint)
            step+=num_images-2
        j+=1
    # print(transpose_constraint)
    return transpose_constraint

def binary_prog(interest_matrix):
    num_images = interest_matrix.shape[0]
    num_elements = num_images*num_images - num_images
    c = np.zeros(num_elements)
    itr = 0
    for i in range(0, num_images):
        for j in range(0, num_images):
            if i!=j:
                c[itr] = interest_matrix[i,j]
                itr+=1
    # print(interest_matrix, c)
    G = np.zeros((num_images, num_elements))
    A = np.zeros((num_images, num_elements))

    B = set(range(num_elements))
    transpose_constraint = create_transpose_sum_constraint(num_images)
    # return
    g_pos= 0
    for i in range(num_images):
        curr_g = (num_images-1)*g_pos
        G[i, curr_g:curr_g+(num_images-1)] = 1
        for j in range(0, num_elements, num_images-1):
            if i+j<num_elements:
                A[i,i+j]=1
        g_pos+=1

    # A = np.concatenate((A, G), axis=0)
    # A = np.concatenate((A, transpose_constraint), axis=0)
    # print("A", A)
    # print("G", G)
    b = matrix(np.ones(num_images))
    h = matrix(np.ones(num_images))
    c = -1*c
    c = matrix(c)
    A = matrix(A)
    # G = matrix(G)
    G = matrix(G)
    (status, x) = ilp(c=c, G=G, h=h, A=A, b=b, B=B)
    # print(status)
    # x = np.array(x)
    indicator_matrix = create_matrix(x, num_images)
    return indicator_matrix
