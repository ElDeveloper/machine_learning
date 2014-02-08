function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

% them damn parenthesis!
J = (-y'*log(sigmoid(X*theta)) - ((1-y')*log(1-sigmoid(X*theta))))/m + (lambda*sum(theta(2:end).^2))/(2*m);

% we have to do it like this to respect the gradient descent algorithm where
% the value of J equal to zero does not require any regularization, see the
% the notes or the lecture
temp = (X'*(sigmoid(X*theta)-y))/m;
grad(1) = temp(1);

temp = (X'*(sigmoid(X*theta)-y))/m + (lambda/m)*theta;
grad(2:end) = temp(2:end);



% =============================================================

end
