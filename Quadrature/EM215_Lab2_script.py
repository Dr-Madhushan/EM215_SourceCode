import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (4/(x**2 + 1))

#__________________________________________________________________________________________________________________

def trapazoid(n, a, b):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + (i*h))
    result = result * h / 2
    return result

#__________________________________________________________________________________________________________________

def simpson(n, a, b):
    h = (b - a) / n
    result = f(a) + f(b)
    r1 = 0
    r2 = 0
    for i in range(1, n):
        if(i%2 == 0):
            r2 += f(a + (i*h))
        else:
            r1 += f(a + (i*h))
    
    result = (result + (4 * r1 + 2 * r2)) * (h / 3)

    return result

#__________________________________________________________________________________________________________________

def gaussianQuadrature(a, b):
    nodes = [-math.sqrt(3/5), 0, math.sqrt(3/5)]
    weights = [(5/9), (8/9), (5/9)]

    result = 0
    for i in range(3):
        result += weights[i] * f(nodes[i]*(b-a)/2 + (a+b)/2)
    result *= (b-a)/2

    return result

#__________________________________________________________________________________________________________________

def comp_gaussQuadrature(n, a, b):
    intervals = list(np.linspace(a,b,n+1))
    result = 0
    for i in range(n):
        result += gaussianQuadrature(intervals[i], intervals[i+1])
    return result

#__________________________________________________________________________________________________________________

def romberg(a, b, t, type):
    Rs = []
    Es = []
    r = []
    e = []
    exact = math.pi
    
    for i in range(t):
        if type == "trapazoid":
            p = trapazoid((2**i), a, b)
        elif type == "simpson":
            p = simpson((2**i), a, b)
        r.append(p)
        e.append(exact-p)
    Rs.append(r)
    Es.append(e)

    for k in range(t-1):
        r = []
        e = []
        for j in range(1, t-k):
            v = Rs[-1][j] + ((Rs[-1][j] - Rs[-1][j-1])/(4**(k+1) - 1))
            r.append(v)
            e.append(exact-v)

        Rs.append(r)
        Es.append(e)

    return [Rs,Es]

# Q1 __________________________________________________________________________________________________________________
# To print the Romberg table for trapezoidal rule
[Rs, Es] = romberg(0,1,4, "trapazoid")

print("Trapazoid\n")
print("Romberg Table of approximations")
for i in Rs:
    print(i)
print("")
print("Table of error")
for i in Es:
    print(i)

# To print the Romberg table for Simpson's rule
[Rs, Es] = romberg(0,1,4, "simpson")

print("\nSimpson\n")
print("Romberg Table of approximations")
for i in Rs:
    print(i)
print("")
print("Table of error")
for i in Es:
    print(i)

n_lst = [10,20,40,60,80]


# To compare the error and approximation of each rule print

print(" n          trapezoidal              trap_error               simpson               simp_error")
print("====================================================================================================")
for n in n_lst:
    trapAprx = trapazoid(n,0,1)
    simpAprx = simpson(n,0,1)
    exact = math.pi
    print(n," | ", trapAprx," | ", exact-trapAprx, " | ", simpAprx, " | ", exact-simpAprx)

#__________________________________________________________________________________________________________________


# Functions to plot and compare the errors

def comp_error_TrapAndSimpson(n_lst, a, b):
    trapError_arr = []
    simpError_arr = []
    h_arr = []
    for n in n_lst:
        trapAprx = trapazoid(n,a,b)
        simpAprx = simpson(n,a,b)
        exact = math.pi
        trapError_arr.append(math.log(exact-trapAprx))
        simpError_arr.append(math.log(exact-simpAprx))
        _h = (b - a) / n
        h_arr.append(math.log(_h))

    y1 = np.array(trapError_arr)
    y2 = np.array(simpError_arr)
    h = np.array(h_arr)

    plt.plot(h,y1, 'bo-')
    plt.plot(h,y2,'ro-')
    plt.title("Plots log(Trapazoidal Error) & log(Simpson's Error) vs log(h)")
    plt.xlabel("log(h)")
    plt.ylabel("log(Error)")
    plt.legend(["Trapazoidal Error - log curve", "Simpson's Error - log curve"])
    plt.grid()
    plt.show()

comp_error_TrapAndSimpson(n_lst, 0, 1)      #function call

#__________________________________________________________________________________________________________________


def plot_GaussError_vs_h(n_lst, a, b):
    y = []
    h_arr = []
    for n in n_lst:
        gaussAprx = comp_gaussQuadrature(n,a,b)
        exact = math.pi
        _h = (b - a) / n
        h_arr.append(math.log(_h))
        y.append(math.log(exact-gaussAprx))

    plt.plot(np.array(h_arr),np.array(y),'go-')
    plt.title("Plots log(Gaussian Quadrature Error) vs log(h)")
    plt.xlabel("log(h)")
    plt.ylabel("log(Error)")
    plt.grid()
    plt.show()

plot_GaussError_vs_h(n_lst, 0, 1)   #function call

#__________________________________________________________________________________________________________________


def comp_error_GaussAndSimpson(n_lst, a, b):
    gaussError_arr = []
    simpError_arr = []
    h_arr = []
    for n in n_lst:
        gaussAprx = comp_gaussQuadrature(n,a,b)
        simpAprx = simpson(n,a,b)
        exact = math.pi
        gaussError_arr.append(math.log(exact-gaussAprx))
        simpError_arr.append(math.log(exact-simpAprx))
        _h = (b - a) / n
        h_arr.append(math.log(_h))

    y1 = np.array(gaussError_arr)
    y2 = np.array(simpError_arr)
    h = np.array(h_arr)

    plt.plot(h, y1, 'go-')
    plt.plot(h, y2, 'ro-')
    plt.title("Plots log(Gaussian Error) & log(Simpson's Error) vs log(h)")
    plt.xlabel("log(h)")
    plt.ylabel("log(Error)")
    plt.legend(["Gaussian Error - log curve", "Simpson's Error - log curve"])
    plt.grid()
    plt.show()

comp_error_GaussAndSimpson(n_lst, 0, 1)     #function call

#__________________________________________________________________________________________________________________

