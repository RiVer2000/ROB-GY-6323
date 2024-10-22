import sympy as sp

def symbolic_gradient(f, variables):
    """
    Compute the symbolic gradient (partial derivatives) of a function.
    """
    gradient = [sp.diff(f, var) for var in variables]
    return gradient

def symbolic_hessian(f, variables):
    """
    Compute the symbolic Hessian matrix (second-order partial derivatives) of a function.
    """
    hessian = sp.Matrix([[sp.diff(f, var1, var2) for var2 in variables] for var1 in variables])
    return hessian

# Define symbolic variables
x, y, z = sp.symbols('x y z')

# Define the functions from the image
f1 = -sp.exp(-(x - 1)**2)
f2 = (1 - x)**2 + 100 * (y - x**2)**2
f3 = sp.Matrix([x, y]).T * sp.Matrix([[3, 1], [1, 3]]) * sp.Matrix([x, y]) + sp.Matrix([1, -1]).T * sp.Matrix([x, y])
f4 = 1/2 * sp.Matrix([x, y, z]).T * sp.Matrix([[1, 1, 0], [1, 1, 0], [0, 0, 4]]) * sp.Matrix([x, y, z]) - sp.Matrix([0, 0, 1]).T * sp.Matrix([x, y, z])

# Calculate gradients
grad_f1 = symbolic_gradient(f1, [x])
grad_f2 = symbolic_gradient(f2, [x, y])
grad_f3 = symbolic_gradient(f3, [x, y])
grad_f4 = symbolic_gradient(f4, [x, y, z])

print("Gradient of f1:")
sp.pprint(grad_f1)
print("Gradient of f2:")
sp.pprint(grad_f2)
print("Gradient of f3:")
sp.pprint(grad_f3)
print("Gradient of f4:")
sp.pprint(grad_f4)


# Calculate Hessians
hess_f1 = symbolic_hessian(f1, [x])
hess_f2 = symbolic_hessian(f2, [x, y])
hess_f3 = symbolic_hessian(f3, [x, y])
hess_f4 = symbolic_hessian(f4, [x, y, z])

print("Hessian of f1:")
sp.pprint(hess_f1)
print("Hessian of f2:")
sp.pprint(hess_f2)
print("Hessian of f3:")
sp.pprint(hess_f3)
print("Hessian of f4:")
sp.pprint(hess_f4)
