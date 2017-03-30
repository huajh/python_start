function [u] = heat(f)

% The Heat Equation
% Input: Original grayscale image u0
% Output: Evolved image u

%Parameters
dt = 0.2;  %Time step
T = 20;  %Final time

f = double(f);
u = f;
[m,n] = size(u);

%This draws the image every iteration, which slows down the program.
for t = 0:dt:T
    u_xx = u(:,[2:n,n]) - 2*u(:,:) + u(:,[1,1:n-1]);
    u_yy = u([2:m,m],:) - 2*u(:,:) + u([1,1:m-1],:);
    u(:,:) = u(:,:) + dt*(u_xx + u_yy);
    subplot(121); imshow(uint8(f)); title('Original');
    subplot(122); imshow(uint8(u)); title(['Time t=',num2str(t)]);
    colormap gray;
    drawnow;
end;