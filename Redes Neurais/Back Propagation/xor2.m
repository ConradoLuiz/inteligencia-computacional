function xor2

P = [0 0 1 1; 0 1 0 1];
T = [0 1 1 0];

net = newff([min(P')' max(P')'], [2 1], {'logsig', 'purelin'}, 'traingd');

net.trainParam.epochs = 1000;
net.trainParam.goal = 1e-3;
net.trainParam.lr = 0.01;
net.trainParam.show = 25;

net = train(net, P, T);

C = sim(net, P)

figure
subplot(1,2,1)
hold on
for i = 1:4,
   if (T(i) > 0.5)
      plot(P(1,i), P(2,i), 'b.')
   else
      plot(P(1,i), P(2,i), 'r.')
   end
end
xlim([-1 2])
ylim([-1 2])
axis square
set(gca, 'xtick', [0 1])
set(gca, 'ytick', [0 1])
box on
title('Desejado')

subplot(1,2,2)
hold on
for i = 1:4,
   if (C(i) > 0.5)
      plot(P(1,i), P(2,i), 'b.')
   else
      plot(P(1,i), P(2,i), 'r.')
   end
end
xlim([-1 2])
ylim([-1 2])
axis square
set(gca, 'xtick', [0 1])
set(gca, 'ytick', [0 1])
box on
title('Obtido')