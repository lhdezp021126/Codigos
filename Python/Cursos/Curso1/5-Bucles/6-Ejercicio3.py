import math;

for i in range(11):
    print(i);
    
num1=int(input('Insert a number: '));
num2=int(input('Insert a number: '));

min=min(num1,num2);
max=max(num1,num2);

for i in range(min,max):
    print(i);