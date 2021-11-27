
#A. UNA LLAVE QUE SE HABRE 4 HORAS, VIERTE 1200 LITROS DE AGUA. REALIZAR
#UN PROGRAMA QUE CALCULE CUANTA AGUA VIERTE LA LLAVE EN CUALQUIER
#NUMERO DE HORAS.

horas = float(input("Ingrese el numero de horas:"))
x = 1200 / 4
totalagua = horas * x
print("El total de litros de agua en ciertas horas es:" + str(totalagua))