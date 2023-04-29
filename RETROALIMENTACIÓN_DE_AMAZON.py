#Esta importación funciona para cerrar algun programa con el acompañamiento de .exit() ejemplo: sys.exit()
import sys
#RETROALIMENTACIÓN_DE_AMAZON
a=("\nEn DEPORTES Tenemos:\n1.Zapatillas deportivas\n2.Guantes de beisball.\n3.Pelota de futball.\n4.Raqueta de tenis.\n5.Bola de basketball.")
b=("\nEn VIAJES Tenemos:\n1.Maletas.\n2.Bufandas.\n3.Ropa de viaje.\n4.Almohada de cuello.\n5.Abrigos.")
c=("\nEn MEDICINA Tenemos:\n1.pastillas para el dolor de cabeza.\n2.pastillas para la presión.\n3.pastillas para la fiebre\n4.Vendas\n5.Inyecciones.")
d=("\nEn VIDEOJUEGOS Tenemos:\n1.Playstation 6.\n2.GTA6.\n3.call of Duty.\n4.Controles de play.\n5.Mario Party.")
#deportes
A="Tiene un costo de 20$"
B="Tiene un costo de 21.99$"
C="Tiene un costo de 45$"
D="tiene un costo de 30$"
E="Tiene un costo de 67.99$"
#viajes
F="Tiene un costo de 15$"
G="Tiene un costo de 10.99$"
H="Tiene un costo de 100$"
I="tiene un costo de 26$"
J="Tiene un costo de 70$"
#medicinas
K="Tiene un costo de 2.50$ x Capsulas"
L="Tiene un costo de 3.35$ x capsulas"
M="Tiene un costo de 3.67$ x capsulas"
N="tiene un costo de 5.34$"
O="Tiene un costo de 30$ cada una."
#video juegos
P="Tiene un costo de 450$"
Q="Tiene un costo de 95$"
R="Tiene un costo de 40$"
S="tiene un costo de 50$ cada uno."
T="Tiene un costo de 35$"
#Este espacio es para celeccionar la categoría
print("\nAMAZON.COM\n\nEstas son las secciones de productos que les ofrecemos por el momento\nSeleccione con el número que le corresponde a cada sección:")
dec=input("1.Deportes\n2.Viajes\n3.Medicina\n4.Videojuegos\n\n¿En cual está interesado usted?")
if dec=="1":
    print(a)
elif dec=="2":
    print(b)
elif dec=="3":
    print(c)
elif dec=="4":
    print(d)
elif dec=="no":
    print("Gracias por su tiempo, vuelva pronto.")
    input("")
    sys.exit()
else:
    print("Error, vuelva a intentarlo.")
    input("")
#Comandos de DEPORTES
dec2=input("\nRECOMENDACIÓN: Para seleccionar alguna ponga el numero de su fila\n¿Desea alguna? y si no desea nada solo ponga > No")
if dec2=="1":
    print(A)
elif dec2=="2":
    print(B)
elif dec2=="3":
    print(C)
elif dec2=="4":
    print(D)
elif dec2=="5":
    print(E)
#Este "elif" tiene integrada una importación llamada: sys.exit() que nos permite salir del programa.(se repite en todos los comandos)
elif dec2=="no":
    print("Gracias por su tiempo, vuelva pronto.")
    input("")
    sys.exit()
else:
    print("Error, vuelva a intentarlo.")
    input("")
#Comando de VIAJE
viaje=input("\nRECOMENDACIÓN: Para seleccionar alguna ponga el numero de su fila\n¿Desea alguna? y si no desea nada solo ponga > No")
if viaje=="1":
    print(F)
elif viaje=="2":
    print(G)
elif viaje=="3":
    print(H)
elif viaje=="4":
    print(I)
elif viaje=="5":
    print(J)
elif viaje=="no":
    print("Gracias por su tiempo, vuelva pronto.")
    input("")
    sys.exit()
else:
    print("Error, vuelva a intentarlo.")
    input("")
#Comando de MEDICINA
medi=input("\nRECOMENDACIÓN: Para seleccionar alguna ponga el numero de su fila\n¿Desea alguna? y si no desea nada solo ponga > No")
if medi=="1":
    print(K)
elif medi=="2":
    print(L)
elif medi=="3":
    print(M)
elif medi=="4":
    print(N)
elif medi=="5":
    print(O)
elif medi=="no":
    print("Gracias por su tiempo, vuelva pronto.")
    input("")
    sys.exit()
else:
    print("Error, vuelva a intentarlo.")
    input("")
#Comando de VIDEO JUEGO
vj=input("\nRECOMENDACIÓN: Para seleccionar alguna ponga el numero de su fila\n¿Desea alguna? y si no desea nada solo ponga > No")
if vj=="1":
    print(P)
elif vj=="2":
    print(Q)
elif vj=="3":
    print(R)
elif vj=="4":
    print(S)
elif vj=="5":
    print(T)
elif vj=="no":
    print("Gracias por su tiempo, vuelva pronto.")
    input("")
    sys.exit()
else:
    print("Error, vuelva a intentarlo.")
    input("")