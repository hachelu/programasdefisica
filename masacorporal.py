
#PROGRAMA QUE CALCULA EL IMC (INDICE DE MASA CORPORAL) DE UNA PERSONA.

peso = float(input("Ingresa tu peso en [Kg]:"))
estatura = float(input("Ingresa tu estatura en [m]:"))

imc = peso / (estatura**2)

print("Su indice de masa corporal es:" + str(imc))

if (imc < 18.5):
 print("Su peso es bajo")
elif (18.5 <= imc and imc < 25):
    print("Su peso es normal")

elif (25 <= imc and imc < 30): 
 print("Usted tiene sobre peso")  

else:
 print("Usted tiene obesidad")
