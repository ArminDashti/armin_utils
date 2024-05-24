# This code was generated by OpenAI ChatGPT 3.5

import numpy as np


def conjugate_gradient(A, b, x0, tol=1e-6, max_iter=1000):
    """
    Solve the linear system Ax = b using the Conjugate Gradient method.

    Parameters:
        A (numpy.ndarray): The coefficient matrix.
        b (numpy.ndarray): The right-hand side vector.
        x0 (numpy.ndarray): The initial guess for the solution.
        tol (float): Tolerance for convergence. Default is 1e-6.
        max_iter (int): Maximum number of iterations. Default is 1000.

    Returns:
        numpy.ndarray: The solution vector x.
    """
    x = x0
    r = b - A.dot(x)
    p = r
    r_dot_old = np.dot(r, r)
    for i in range(max_iter):
        Ap = A.dot(p)
        alpha = r_dot_old / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        r_dot_new = np.dot(r, r)
        if np.sqrt(r_dot_new) < tol:
            break
        beta = r_dot_new / r_dot_old
        p = r + beta * p
        r_dot_old = r_dot_new
    return x

A = np.array([[4, -1], [-1, 3]])
b = np.array([5, 3])
x0 = np.array([0, 0])
solution = conjugate_gradient(A, b, x0)
print("Solution:", solution)
