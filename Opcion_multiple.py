
import sys

print ("Bienvenido a opción multiple sobre Amazon y el Big data!");
print ("\nIndícanos tu nombre para poder empezar.\n");
people = input("Ponga su nombre: ");
print ("\nBien " + people + " empecemos pero antes unas instrucciones:\n");
print("UNICAMENTE UTILICE LAS LETRAS ASIGNADAS (a, b, c y d.) DE SER LO CONTRARIO SE CERRARÁ EL PROGRAMA AUTOMÁTICAMENTE!");
input("\nPrecione Enter para empezar.\n");
#AREA DE PREGUNTAS.
p1 = "¿Qué tipo de datos utiliza Amazon para mejorar la experiencia de compra de sus clientes?\na) Datos demográficos.\nb) Datos de interacción con el sitio web.\nc) Datos de compra.\nd) Todas las anteriores.\n"
p2 = "¿Qué tipo de servicios ofrece Amazon Web Services (AWS)?\na) Infraestructura de tecnología de la información.\nb) Plataforma como servicio.\nc) Software como servicio.\nd) Todas las anteriores.\n"
p3 = "¿Qué tipo de datos utiliza Amazon para optimizar sus operaciones logísticas?\na) Datos de inventario.\nb) Datos de envío.\nc) Datos de entrega.\nd) Todos los anteriores.\n"
p4 = "¿Cómo utiliza Amazon Big Data para mejorar sus servicios de atención al cliente?\na) Analizando los datos de interacción con los clientes.\nb) Prediciendo el comportamiento del consumidor.\nc) Detectando patrones de fraude.\nd) Todas las anteriores.\n"
#AREA DE CONDICIONALES Y ESTRUCTURA SECUENCIALES.
r1 = input (p1);
if r1 == "d":
    print ("Correcto!");
elif r1 == "a":
    print("Incorrecto!");
elif r1 == "b":
    print("Incorrecto!");
elif r1 == "c":
    print("Incorrecto!");
else:
    print ("SIGA INDICACIONES!!!");
    input("");
    sys.exit();

r2 = input (p2);
if r2 == "d":
    print ("Correcto!");
elif r2 == "a":
    print("Incorrecto!");
elif r2 == "b":
    print("Incorrecto!");
elif r2 == "c":
    print("Incorrecto!");
else:
    print ("SIGA INDICACIONES!!!");
    input("");
    sys.exit();

r3 = input (p3);
if r1 == "d":
    print ("Correcto!");
elif r3 == "a":
    print("Incorrecto!");
elif r3 == "b":
    print("Incorrecto!");
elif r3 == "c":
    print("Incorrecto!");
else:
    print ("SIGA INDICACIONES!!!");
    input("");
    sys.exit();

r4 = input (p4);
if r4 == "a":
    print ("Correcto!");
elif r4 == "b":
    print("Incorrecto!");
elif r4 == "c":
    print("Incorrecto!");
elif r4 == "d":
    print("Incorrecto!");
else:
    print ("SIGA INDICACIONES!!!");
    input("");
    sys.exit();

