P1=float(input("Insert the value of the practic one: "));
P2=float(input("Insert the value of the practic two: "));
P3=float(input("Insert the value of the practic three: "));
EP=float(input("Insert the value of the parcial exam: "));
EF=float(input("Insert the value of the final exam: "));

PP = ( P1 + P2 +P3 ) / 3 ;
PROM = ( PP + 2*EP + 3*EF ) / 6;
print("The final average is ",PROM);