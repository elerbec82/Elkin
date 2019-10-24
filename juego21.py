from funciones import *

def juego():
    userP = 0
    maqP = 0
    jugar = "si"
    while jugar == "si":
        numTur = 1
        numU = 0
        numC = 0
        while True:
            
            if numTur == 1:
                print("-----------||------------")
                print("Turno "+ nombre + " :                        Turno MAQUINA: ")
                print("Cartas "+ nombre + ": " + str(turno("user")) +"           Cartas MAQUINA: [" + str(turno("maquina")[0]) + ", --]")
                numU += suma(0, 0, "user")
                print("Resultado "+ nombre + " es: " +str(numU))
                print("-----------||------------||||---------------||----------------")
                print("-----------||------------||||---------------||----------------")
                #print("Turno MAQUINA: ")
                #print("Cartas maquina: " + str(turno("maquina")[0]) + ", --")
                #print("Cartas MAQUINA: " + str(turno("maquina")))
                numC += suma(0, 0, "maquina")
                numTur +=1
                #print("Resultado MAQUINA es: " +str(numC))
            else:
                print("Turno No"+ str(numTur)+" "+ nombre + ": ")
                numTur +=1
                des = input("Desea otra carta si o no? : ")
                if des == "si":
                    print("-----------||------------")
                    print (turno("user"))
                    numU = suma(numU, len(user())-1, "user")
                    print("Resultado "+ nombre + " es: " +str(numU))
                    print("-----------||------------")
                    if numU >21:
                        break
                des2 = input("Deseas plantar tu juego si o no? : ")
                if des2 == "si":
                    print("-----------| EL JUGADOR "+ nombre + " SE HA PLANTADO |------------")
                    break
        
        while True:
            desC = random.choice(["Si", "No"])
            if (desC == "Si" and numC < 21) or numC <=10:
                print("-----------||------------")
                print("otra carta para MAQUINA")
                print("-----------||------------")
                print(turno("maquina"))
                numC = suma(numC, len(pc())-1, "maquina")
                #print("longitud pc: " + str(len(pc())))
            elif desC == "No" or numC == 21 or numC > 21:
                print("-----------||------------")
                print("Cartas MAQUINA: " + str(pc()))
                print("Resultado MAQUINA es: " +str(numC))
                print("-----------| LA MAQUINA SE HA PLANTADO |------------")
                break
        userP, maqP = validarGanador(numU, numC, userP, maqP)
        #userP += userP
        #maqP += maqP
        print("El puntaje es: " + nombre + " con "+ str(userP) + "----||--- MAQUINA con " + str(maqP))
        jugar = input("Desea jugar de nuevo si o no ?")
print (juego())
