#B. PROGRAMA QUE CALCULA EL PROMEDIO DE UN ESTUDIANTE QUE CURSA LAS
#SIGUIENTES MATERIAS: METROLOGIA, ALGEBRA, CALCULO, ECONOMIA,
#ESTADISTICA, ESTUDIO DEL TRABAJO.

mat1 = float(input("Inserte la nota de la materia metrologia:"))
mat2 = float(input("Inserte la nota de la materia algebra:"))
mat3 = float(input("Inserte la nota de la materia calculo:"))
mat4 = float(input("Inserte la nota de la materia economia:"))
mat5 = float(input("Inserte la nota de la materia estadistica:"))
mat6 = float(input("Inserte la nota de la materia estudio del trabajo:"))

promedioestudiante = (mat1 + mat2 + mat3 + mat4 + mat5 + mat6)/6
print("El promedio final del estudiante es:" + str(promedioestudiante))
