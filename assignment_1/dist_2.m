function dist = dist_2(a,b)
% This function computes the Euclidean distance between vector a and b. If a
% or b is a matrix, all combinations of distances are computed where each row
% corresponds to a different vector. For example if a is an n x d matrix and b
% is an m x d matrix, the output will be an n x m matrix where the i,j entry is
% the distance between row i in a and row j in b. a and b must have the same
% number of columns.

[height_a, width_a] = size(a);
[height_b, width_b] = size(b);

if width_b ~= width_a
  error('The column lengths are not the same');
end

x = diag(a*a');
y = diag(b*b')';
z = 2*(a*b');

dist = sqrt(repmat(x, 1, height_b) + repmat(y, height_a, 1) - z );

end