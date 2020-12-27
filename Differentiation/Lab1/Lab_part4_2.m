% Matlab example for the error with respect to h
function findh()
 
f = @(x) exp(x);
%f=@fun;
x = 1;
f_at = exp(x);
h_grid = logspace(-10,1,50);
f_at_approx = discreteSecondDerivative(f,x,h_grid);
loglog(h_grid,abs(f_at_approx - f_at));
title('Total error of discrete approximation - optimal h demo first')
xlabel('h');
ylabel('R_{total}')
return;
function f_at_approx = discreteSecondDerivative(f,x,h)
f_at_approx = (f(x+h) - 2*f(x) + f(x-h))./h.^2;

return;
