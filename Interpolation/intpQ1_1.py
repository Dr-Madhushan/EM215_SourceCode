import numpy as np
import matplotlib.pyplot as plt

def F(C,x):
    # Derived Polynomial
    res = 0
    for i in range(len(C)):
        res += C[i][0] * (x**i)
    return res

def f(x):
    # Original Polynomial
    return 1 + 10 * x

x = np.linspace(0.1,0.2,11)
y = f(x)

print(x)
print(y)

matrix = []
b = []

# Using Direct Method
# Generate A, b -------------------> A.x = b format
for i in range(len(x)):
    row = []
    b_row = []
    for j in range(len(x)):
        row.append(list(x)[i]**j)
    matrix.append(row)
    b.append([list(y)[i]])

A = np.array(matrix)
b = np.array(b)

# inverse of A
inv = np.linalg.inv(A)
coef = np.dot(inv,b)
print(coef)
f = F(coef, x)
print(f)

# Plot both the curves and the error
plt.plot(x,y, 'bx')
plt.plot(x,f,'r.')
plt.title("Original and Derived Equation Plot")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Original", "Derived"])
plt.grid()
plt.show()

e = abs(y - f)

plt.plot(x,e,'g-')
plt.title("Approximation Error abs(e) vs x")
plt.xlabel("x")
plt.ylabel("abs(e)")
plt.grid()
plt.show()