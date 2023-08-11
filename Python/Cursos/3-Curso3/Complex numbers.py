import cmath;
 
if __name__=='__main__':
    z1=1+3j;
    z2=3+4j;
    print(type(z1));
    print(z1.real);
    print(z1.imag);
    print(z1+z2);
    print(z1-z2);
    print(z1*z2);
    print(z1/z2);
    print(z1.conjugate());
    print(abs(z1));#mod
    print(cmath.phase(z1));#argument
    print(cmath.polar(z1));#polar representation->(mod,arg)
    print(cmath.rect(abs(z1),cmath.phase(z1)));#binomial representation
     