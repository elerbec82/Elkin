
import random
numero = []
while True:
    cantidad = int(input("CANTIDAD DE DIGITOS PARA JUGAR: "))
    if cantidad in [3,4,5]:
        break

while len (numero) < cantidad:
    digito = random.randint (0,9)
    if digito not in numero:
        numero.append(digito)

print (numero)


while True:
    while True:
        intento = input ("INGRESE UN NÚMERO: ")

        usuario = []
        for i in intento:
            if int (i) not in usuario:
                usuario.append(int(i))

        if len (usuario) != len (numero):
            print ("INTENTO NO VALIDO")
        else:
            break

    fijas = 0
    picas = 0

    for i in range(len(numero)):
        if numero [i] == usuario [i]:
            fijas += 1

    for i in range(len(numero)):
        for j in range (len(usuario)):
            if numero [i] == usuario [j] and i != j:
                picas += 1


    print ("FIJAS = " + str (fijas))
    print ("PICAS = " + str (picas))
    if fijas == cantidad:
        print ("FELICITACIONES")
        break







