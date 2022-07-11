function saida = exemplo(a, b)
fprintf('No exemplo: a = %f, b = %f %f\n', a, b)
a = b(1) + 2*a;
b = a .* b;
saida = a + b(1);
fprintf('No exemplo: a = %f, b = %f %f\n', a, b)


a = 2; b = [6 4];
fprintf('Antes do exemplo: a = %f, b = %f %f\n', a, b)
saida = exemplo(a, b);
fprintf('Depois do exemplo: a = %f, b = %f %f\n', a, b)
fprintf('Depois do exemplo: saida = %f\n', saida)