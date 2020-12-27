function forward_centre( )
 
%  Estimate f'(x) over [0,2].

 clear all; 
a = 0.0;
  b = 2.0;
  n = 26;
  x =linspace ( a, b, n );
  yd = fun_deriv ( x );%exact derivative of the function
  h = ( b - a ) / (( n - 1 )*3);
  yp4 = diff_center4 ( 'fun(x)', x, h );
  hold ( 'on' );
  plot ( x, yd, 'b-', 'linewidth', 1 )
  plot ( x, yp4, 'r-', 'linewidth', 1 )
  
  grid ( 'on' );
  hold ( 'on' )
  %  Terminate.
%begin the centered difference
yp = diff_center ( 'fun(x)', x, h );
 
  hold ( 'on' );
  plot ( x, yp, 'g-', 'linewidth', .1 )
 legend ( 'True derivative', 'fourth order centered difference','Second order Centered difference' )
  grid ( 'on' );
  hold ( 'on' )
  
%  Terminate.
return
 end
%This function uses the following functions: 
function y = fun ( x )
 %This is your function.Change it as you wish.
y = 1.0 ./ ( ( x - 0.3 ).^2 + 0.01 ) ...
    + 1.0 ./ ( ( x - 0.9 ).^2 + 0.04 ) ...
    - 6.0;
    return
end
%****************************************************
function yp = fun_deriv ( x )
 %% fun_deriv evaluates the derivative of the function.
  yp = - 2.0 .* ( x - 0.3 ) ./ ( ( x - 0.3 ).^2 + 0.01 ).^2 ...
       - 2.0 .* ( x - 0.9 ) ./ ( ( x - 0.9 ).^2 + 0.04 ).^2;
  return
end
function yp = diff_forward ( f_string, x, h )
 
%% diff_forward uses forward differences to estimate f'(x).
%

  f_element = vector_to_element ( f_string );
  f = str2func ( [ '@(x)', f_element ] );
 
  if ( nargin < 2 )
    
( ischar ( x ) )
    x = str2num ( x );
  end
 
  if ( nargin < 3 )
    
( ischar ( h ) )
    h = str2num ( h );
  end
 
  n = length ( x );
  yp = zeros ( n, 1 );
  for i = 1 : n
    yp(i) = ( f ( x(i) + h ) - f ( x(i) ) ) / h; 
  end
 
  return
end
function f_element = vector_to_element ( f_vector )

%% vector_to_element rewrites a MATLAB vector function element wise.
%
%  Discussion:
%
%    In MATLAB, by default, the operators '*', '/', and '^' are interpreted
%    as linear algebraic operations.  In many cases, a user simply desired
%    the elementwise operation instead, which MATLAB indicates using a 
%    dotted notation: '.*', './', and '.^'.
%
%    This function converts a string to a form that uses dotted operators.
%  Input:
%
%    string f_vector, a string presumably representing a MATLAB expression.
%
%  Output:
%
%    string f_element, a copy of f_vector in which all operators have been
%    replaced by their dotted (elementwise) form.
%
  n_vector = length ( f_vector );
  f_element = [''];
 
  c_prev = '';
  for iv = 1 : n_vector
    c = f_vector(iv);
    if ( ( c == '*' || c == '/' || c == '^' ) && ( c_prev ~= '.' ) )
      f_element = [ f_element, ' .', c, ' ' ];
    else
      f_element = [ f_element, c ];
    end
    c_prev = c;
  end
 
  return
end
function yp = diff_center ( f_string, x, h )
 
%*****************************************************************************80
%
%% diff_center uses centered differences to estimate f'(x).
f_element = vector_to_element ( f_string );
  f = str2func ( [ '@(x)', f_element ] );
 
  if ( nargin < 2 )
    
( ischar ( x ) )
    x = str2num ( x );
  end
 
  if ( nargin < 3 )
    ( ischar ( h ) )
    h = str2num ( h );
  end
 
  n = length ( x );
  yp = zeros ( n, 1 );
  for i = 1 : n
%formula for second order centered difference
    yp(i) = ( f ( x(i) + h ) - f ( x(i) - h ) ) / 2.0 / h; 
  end
 
  return
end

function yp4 = diff_center4 ( f_string, x, h )
%% diff_center uses centered differences to estimate f'(x).
f_element = vector_to_element ( f_string );
  f = str2func ( [ '@(x)', f_element ] );
 
  if ( nargin < 2 )
    
( ischar ( x ) )
    x = str2num ( x );
  end
 
  if ( nargin < 3 )
    ( ischar ( h ) )
    h = str2num ( h );
  end
 
  n = length ( x );
  yp4 = zeros ( n, 1 );
  for i = 1 : n
%formula for second order centered difference
    yp4(i) = ( - f ( x(i) + 2*h ) + 8*f ( x(i) + h ) - 8*f ( x(i) - h ) + f ( x(i) - 2*h ) ) / 12.0 / h; 
    
  end
 
  return
end

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
end

%%function f_element = vector_to_element ( f_vector )
%  n_vector = length ( f_vector );
%  f_element = [''];
% 
%  c_prev = '';
%  for iv = 1 : n_vector
%    c = f_vector(iv);
%    if ( ( c == '*' || c == '/' || c == '^' ) && ( c_prev ~= '.' ) )
%      f_element = [ f_element, ' .', c, ' ' ];
%    else
%      f_element = [ f_element, c ];
%    end
%    c_prev = c;
%  end
 
%  return
%end
%