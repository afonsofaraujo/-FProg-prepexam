x=0:0.5:1;
tic
y=3.*x.^2-4.*x+1;
yt=toc;

tic
for i=1:length(x)
    yf=3*x(i)^2-4*x(i)+1;
end
yft=toc;
fprintf('%f\n%f',yt,yft)  %format in %f (float) para 2 digitos %2d




