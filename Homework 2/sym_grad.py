from sympy import init_printing, symbols, exp, Matrix, pprint, simplify, diff
init_printing()
x, y, z = symbols('x y z')
f1 = -exp(-(x-1)**2)
f2 = (1-x)**2 + 100 * (y-x**2)**2
f3 = (Matrix([x, y]).T * Matrix([[3,1], [1,3]]) * Matrix([x, y]) + Matrix([-1, 1]).T * Matrix([x,y])).doit()
f4 = (1/2 * Matrix([x, y, z]).T * Matrix([[1, 1, 0],[1, 1, 0], [0, 0, 4]]) * Matrix([x, y, z]) - Matrix([0, 0, 1]).T * Matrix([x, y, z])).doit()
# pprint(f4)

def gradient(f, variables):
    grad_f = Matrix([simplify(diff(f, var)) for var in variables])
    return grad_f

def hessian(f, variables):
    hess_f = Matrix([[simplify(diff(f, var1, var2)) for var2 in variables] for var1 in variables])
    return hess_f

# Calculate Gradients
grad_f1 = gradient(f1, [x])
grad_f2 = gradient(f2, [x, y])
grad_f3 = gradient(f3, [x, y])
grad_f4 = gradient(f4, [x, y, z])

print("Gradient of f1:")
pprint(grad_f1)
print("Gradient of f2:")
pprint(grad_f2)
print("Gradient of f3:")
pprint(grad_f3)
print("Gradient of f4:")
pprint(grad_f4)

# Calculate Hessians
hess_f1 = hessian(f1, [x])
hess_f2 = hessian(f2, [x, y])
hess_f3 = hessian(f3, [x, y])
hess_f4 = hessian(f4, [x, y, z])

print("Hessian of f1:")
pprint(hess_f1)
print("Hessian of f2:")
pprint(hess_f2)
print("Hessian of f3:")
pprint(hess_f3)
print("Hessian of f4:")
pprint(hess_f4)
