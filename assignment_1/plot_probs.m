function plot_probs()

figure

hist(normrnd(55, 12, 1000,1), 20)
xlabel('Sample Value')
ylabel('Frequency')


end