# x = [i for i in range(-2,3,1)]
x = [i for i in range(-1,2,1)]
u = [i for i in range(-1,2,1)]


def f(x_n, u_n):
    condition = -x_n + 1 + u_n 
    if (-2 <= condition <= 2):
        x_n1 = condition
    elif (condition > 2):
        x_n1 = 2
    else:
        x_n1 = -2
    return x_n1

def J(x, u):
    return 2*abs(x) + abs(u)

def J(x: list, u:list):
    mini_J = 0
    for i in range(3):
        mini_J += 2*abs(x[i]) + abs(u[i])
        print(mini_J)
    
    cost = x[-1]**2 + mini_J
    return cost

def update(xi: int, ui:list):
    # We have three types of control signals -1, 0, 1
    # Control signal u = -1
    x_values = [xi]
    for i in range(3):
        xi = f(xi, ui)
        x_values.append(xi)
    return J(x_values, [ui]*3)
print(update(-2, -1))