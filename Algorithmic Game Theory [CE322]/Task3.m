A = [[1 1 0 0 0 0 0 0 0]; 
[-3 0 0.5 0 0 0 0 0 0];
[0 0 0 -1 -1 0 0 0 0];
[0 0 0 -4 -1 0.5 0 0 0];
[0 0 0 0 0 0 3 0 -0.5];
[0 0 0 0 0 0 4 1 -0.5]; 
 
[1 0 0 1 0 0 0 0 0];
[-3 0 0 0 0 0 0.5 0 0];
[0 -1 0 0 -1 0 0 0 0];
[0 -4 0 0 -1 0 0 0.5 0];
[0 0 3 0 0 0 0 0 -0.5];
[0 0 4 0 0 1 0 0 -0.5]];


f = [-6 -4 0 -4 -2 0 0 0 -1];
b = [0;0;0;0;0;0;0;0;0;0;0;0];
Aeq = [1 1 1 1 1 1 1 1 1];
beq = 1;
lb = [0 0 0 0 0 0 0 0 0];
ub = [1 1 1 1 1 1 1 1 1];

[x,fval]= linprog(f,A,b,Aeq,beq,lb,ub)