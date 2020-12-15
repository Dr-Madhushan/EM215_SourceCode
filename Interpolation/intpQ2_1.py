# Newton's Divided Difference Method
import numpy as np
import matplotlib.pyplot as plt

def func(fxi, fxj, xi, xj):
    '''
        returns the divided difference value
    '''
    return ((fxi - fxj)/(xi - xj))

def nddiff(X, Y, k):
    '''
        X = [x1, x2, x3, x4,....]
        Y = [y1, y2, y3, y4,....]
    '''
    table = []  # initiate empty list
    table.append(list(X[k:]))   # add first and second column in the DD table
    table.append(list(Y[k:]))
    
    for i in range(len(table[0])-1):
        fdd = []
        for j in range(len(table[-1])-1):
            fdd_val = func(table[-1][j], table[-1][j+1], table[0][j], table[0][i+j+1])
            fdd.append(fdd_val)
        table.append(fdd)
    return table

X = [1, 4, 6, 5]
Y = [0, 1.386294, 1.791759, 1.609438]
X = [0,1,3]
Y = [1,2,10]

table = nddiff(X,Y,0)
#print(table)
coef = []
for n in range(1,len(table)):
    coef.append(table[n][0])
#print(coef)

def compute_y(X, Y, x, i):
    '''
        from ith values from X, Y will be used to find the DD table 
        and then coefficients will be picked from table
        Using the coefficients y will be calculated for given x
    '''
    table = nddiff(X, Y, i)
    coef = []
    for n in range(1,len(table)):
        coef.append(table[n][0])
    
    y = 0
    for p in range(len(coef)):
        t = coef[p]
        for j in range(p):
            t = t * (x - list(X)[j])
        y += t
    return y

# 20 x values between -10 and +10
new_x = np.linspace(-10, 10, 20)
# corresponding 20 y values
new_y = np.exp(-1*(new_x**2))
#print("x = ", new_x)
#print("y1 = ", new_y1)
x = np.arange(-10, 10.05, 0.05)
y = compute_y(new_x, new_y, x, 0)
y1 = np.exp(-1*(x**2))
#print("x = ", x)
#print("y = ", y)

plt.plot(x,y1, 'b-') # actual curve
plt.plot(x,y,'r-') # interpolated curve
plt.title("Plots Actual vs Divided difference method interpolated")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Actual", "Interpolated"])
plt.grid()
plt.show()


e = abs(y1 - y)

plt.plot(x,e,'g-')
plt.title("Approximation Error abs(e) vs x")
plt.xlabel("x")
plt.ylabel("abs(e)")
plt.grid()
plt.show()


print("       x              y")
print("________________________________________")
for i in range(20):
    #print("%.5f     %.20f"%(new_x[i], new_y1[i]))
    print(new_x[i],"|", new_y[i])
