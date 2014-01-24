function dist = dist_1(a,b)
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

% preallocate memory because we care
dist = zeros(height_b, height_a);

for current_row=1:1:height_b

  % snippet taken from the second lecture
  row_diff = (a - repmat(b(current_row, :), height_a, 1));
  row_dist = sqrt(sum(row_diff .* row_diff, 2));

  dist(current_row, :) = row_dist';
end

dist = dist';

end