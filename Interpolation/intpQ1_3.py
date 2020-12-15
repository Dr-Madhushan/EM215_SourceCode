import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1/(1+25*(x**2)))

x = np.arange(-1, 1.1, 0.1)
#x = np.array([-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
y = f(x)
print(f(0))
# for i in range(len(x)):
#     print("( ", x[i],", ",y[i]," )")
# print(y)

def lagrange(xi_arr, yi_arr, a):
    '''
        returns the f(a) value for given x = a and coordinate set(xi, yi)
        xi_arr = [x1, x2, x3, x4,...., xn]
        yi_arr = [y1, y2, y3, y4,...., yn]
    '''
    no_coordinates = len(xi_arr)    # number of iterations needed
    appr_fx_val = 0     # final result to be modified

    for i in range(no_coordinates):
        # for each iteration calculate the neumerator and denominator
        unit =  yi_arr[i]
        for j in range(no_coordinates):
            if i != j:
                unit = unit * (a - xi_arr[j])/(xi_arr[i] - xi_arr[j])
        appr_fx_val += unit
    
    return appr_fx_val

new_x = np.arange(-0.5,0.51,0.01)
fx = lagrange(list(x), list(y), new_x)
y = f(new_x)
#print(fx)

plt.plot(new_x,y, 'b-') # actual curve
plt.plot(new_x,fx,'r-') # interpolated curve
plt.title("Plots Actual vs Lagrange interpolated")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Actual", "Interpolated"])
plt.grid()
plt.show()


e = abs(y - fx)

plt.plot(new_x,e,'g-')
plt.title("Approximation Error abs(e) vs x")
plt.xlabel("x")
plt.ylabel("abs(e)")
plt.grid()
plt.show()
