from math import sqrt;
a = float(input('Insert value of a: '));
b = float(input('Insert value of b: '));
c = float(input('Insert value of c: '));
try:
    print('The solutions are: ',((-b+sqrt((b**2)-4*a*c))/2*a),((-b-sqrt((b**2)-4*a*c))/2*a));
except:
    print('No existe solucion en los reales');