partido = input(
    "Inserte candidato A por el partido rojo, "
    + "candidato B por el partido verde, candidato C por el partido azul: "
)
if partido.upper() == "A":
    print("Selecciono al candidato rojo")
elif partido.upper() == "B":
    print("Selecciono al candidato verde")
elif partido.upper() == "C":
    print("Selecciono al candidato azul")
else:
    print("Eligio una opcion invalida")
