import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Se proporcionará una lista de calificaciones de los estudiantes y su tarea es realizar
# análisis estadístico y visualización de datos.
# ● Calcular el promedio de calificaciones para cada asignatura y mostrarlo.
# ● Encuentra a los estudiantes que tienen las calificaciones más altas en cada
# asignatura y mostralos junto con sus respectivas calificaciones.
# ● Calcular el porcentaje de estudiantes que aprobaron cada asignatura (con una
# calificación igual o superior a 60) y mostrar los resultados.
# ● Crear un DataFrame que incluya dos columnas una para las asignaturas y otra
# para la frecuencia de cada calificación.

calificaciones = [
{"nombre": "Juan", "matematicas": 85, "ciencias": 90,
"historia": 75},
{"nombre": "María", "matematicas": 70, "ciencias": 80,
"historia": 85},
{"nombre": "Pedro", "matematicas": 95, "ciencias": 75,
"historia": 90},
{"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia":
80},
{"nombre": "Luis", "matematicas": 75, "ciencias": 70,
"historia": 95},
{"nombre": "Sofía", "matematicas": 90, "ciencias": 85,
"historia": 75},
{"nombre": "Carlos", "matematicas": 85, "ciencias": 90,
"historia": 80},
{"nombre": "Elena", "matematicas": 70, "ciencias": 75,
"historia": 85},
{"nombre": "Javier", "matematicas": 80, "ciencias": 85,
"historia": 90},
{"nombre": "Laura", "matematicas": 75, "ciencias": 70,
"historia": 95},
{"nombre": "Diego", "matematicas": 90, "ciencias": 85,
"historia": 75},
{"nombre": "Paula", "matematicas": 85, "ciencias": 90,
"historia": 80},
{"nombre": "Carmen", "matematicas": 70, "ciencias": 75,
"historia": 85}
]

all_matematica=[]
all_ciencias=[]
all_historia=[]
nota_maxima=13*100
aprobados_matematica=0
may_ciencias=0
may_historia=0
may_matematica=0
aprobados_matematica=[]
aprobados_ciencias=[]
aprobados_historia=[]
fi_mate=[]
fi_ciencias=[]
fi_historia=[]


for i in calificaciones:
    nota_matematica=i["matematicas"]
    all_matematica.append(nota_matematica)

    nota_ciencias=i["ciencias"]
    all_ciencias.append(nota_ciencias)
    nota_historia=i["historia"]
    all_historia.append(nota_historia)

    for nota_mat in range(len(all_matematica)):
            if all_matematica[nota_mat] > may_matematica:
                may_matematica = all_matematica[nota_mat]

    if may_matematica==i["matematicas"]:
          alumno_matematica=i
    
    # if i:
        # fi_mate.append(i["nombre"], i["matematicas"])
        # fi_ciencias.append(i["nombre"], i["ciencias"])
        # fi_historia.append(i["nombre"], i["historia"])

        #   alumno_matematica=i["nombre"], i["matematicas"]

    for nota_ciencia in range(len(all_ciencias)):
            if all_ciencias[nota_ciencia ] > may_ciencias:
                may_ciencias = all_ciencias[nota_ciencia ]

    if may_ciencias==i["ciencias"]:
          alumno_ciencias=i
    
    for nota_historia in range(len(all_historia)):
            if all_historia[nota_historia] > may_historia:
                may_historia = all_historia[nota_historia]

    if may_historia==i["historia"]:
          alumno_historia=i
        
for nota_60_mat in all_matematica:
            if nota_60_mat >= 60:
                aprobados_matematica.append(nota_60_mat)

for nota_60_cien in all_ciencias:
    if nota_60_cien >= 60:
        aprobados_ciencias.append(nota_60_cien)
    
for nota_60_his in all_historia:
    if nota_60_his >= 60:
        aprobados_historia.append(nota_60_his)


print("aprobaron matematica: ", len(aprobados_matematica))
print("aprobaron ciencias: ", len(aprobados_ciencias))
print("aprobararon historia: ", len(aprobados_historia))

print("nota mas alta en matematica: ", alumno_matematica["nombre"], alumno_matematica["matematicas"])
print("nota mas alta en ciencias: ", alumno_ciencias["nombre"], alumno_ciencias["ciencias"])
print("nota mas alta en historia: ", alumno_historia["nombre"], alumno_ciencias["historia"])

print("may_matematica: ", aprobados_matematica)
print("may_ciencias: ", may_ciencias)
print("may_historia: ", may_historia)

print("promedio de los alumnos en matematica", sum(all_matematica) / nota_maxima * 100)
print("promedio de los alumnos en ciencias", sum(all_ciencias) / nota_maxima * 100)
print("promedio de los alumnos en historia", sum(all_historia) / nota_maxima * 100)

fi={}
# for frecuencia in calificaciones:
#     matematica=frecuencia["matematicas"]

# for frecuencia in calificaciones:
#     fi_simple=frecuencia["matematicas"], frecuencia["ciencias"], frecuencia["historia"]  
#     fi[fi_simple]=fi.get(fi_simple, 0)+1

# print(fi_mate)
# print(fi_ciencias)
# print(fi_historia)

df=pd.DataFrame({
      "asignatura": "matematica",
      "fi": fi
})

print(df)

plt.bar(df["asignatura"], df["fi"])
plt.title("Notas de las asignatura")
plt.xlabel("nombres de los estudiantes")
plt.ylabel("promedio de las calificaciones")
# plt.show()
