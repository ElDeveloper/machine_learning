function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

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
%
% Note: grad should have the same dimensions as theta
%

% the most important thing to note here is that the argument to the sigmoid
% function is the transpose of theta multiplied by X, however we don't have
% transpose theta, because theta is already a column vector
J = (-y'*log(sigmoid(X*theta)) - (1-y')*log(1-sigmoid(X*theta)))/m;

% the otherwise summatory function that we would need to evaluate can be
% vectorized if we compute the vector X*theta-y and then multiply it by the
% training set. Note that we transpose X to make it 'multipliable' by the
% other term. This form was noted in the lecture of gradient descent for
% the case of logistic regression as well as in the lecture with Prof. Wilder
grad = (X'*(sigmoid(X*theta)-y))/m;

% =============================================================

end
