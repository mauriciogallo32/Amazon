import sys
verdadero = ""
falso = ""
print ("Bienvenido a verdad o falso sobre AMAZON y EL BIG DATA. \n");
print ("Necesitamos que nos brindes tu nombre porfavor: \n");
#VARIABLE DONDE SE GUARDARÁ LA INFORMACIÓN DE LA PERSONA.
people = input ("Escriba su nombre:");
print ("\nPerfecto " + people + " Te generaremos 6 preguntas de Cierto y falso:\n\nPORFAVOR PONER ESTRICTAMENTE SOLO LAS PALABRAS cierto O faslo !\n");
#PREGUNTAS DE VERDAD Y FALSO.
p1 = "\nAmazon utiliza Big Data para mejorar la experiencia de compra de sus clientes.\n¿Verdadero o falso?"
p2 = "\nAmazon no utiliza Big Data para optimizar sus operaciones logísticas.\n¿Verdadero o falso?"
p3 = "\nAmazon es el mayor proveedor de servicios en la nube.\n¿Verdadero o falso?"
p4 = "\nAmazon no utiliza Big Data para mejorar sus servicios de atención al cliente.\n¿Verdadero o falso?"
p5 = "\nAmazon utiliza Big Data para predecir tendencias de consumo y ajustar sus estrategias de marketing en consecuencia.\n¿Verdadero o falso?"
p6 = "\nAmazon utiliza Big Data para prevenir fraudes en sus transacciones.\n¿Verdadero o falso?"
#ESTRUCTURA SECUENCIALES Y CONDICIONALES + el sys.exit()
verdadero = input (p1 + ":");
if verdadero == "verdadero":
    print ("Correcto!");
elif verdadero == "falso":
    print ("Incorrecto!");
else:
    print ("Porfavor siga indicaciones!!!");
    input("")
    sys.exit()

falso = input (p2 + ":");
if falso == "falso":
    print ("Correcto!");
elif falso == "verdadero":
    print("Incorrecto!");
else:
    print("Porfavor siga indicaciones!!!");
    input("")
    sys.exit()

verdadero = input(p3 + ":");
if verdadero == "verdadero":
    print ("Correcto!");
elif verdadero == "falso":
    print ("Incorrecto!");
else:
    print ("Porfavor siga indicaciones!!!");
    input("")
    sys.exit()

falso = input (p4 + ":");
if falso == "falso":
    print ("Correcto!");
elif falso == "verdadero":
    print("Incorrecto!");
else:
    print("Porfavor siga indicaciones!!!");
    input("")
    sys.exit()

verdadero = input(p5 + ":");
if verdadero == "verdadero":
    print ("Correcto!");
elif verdadero == "falso":
    print ("Incorrecto!");
else:
    print ("Porfavor siga indicaciones!!!");
    input("")
    sys.exit()

verdadero = input(p6 + ":");
if verdadero == "verdadero":
    print ("Correcto!");
elif verdadero == "falso":
    print ("Incorrecto!");
else:
    print ("Porfavor siga indicaciones!!!");
    input("")
    sys.exit()