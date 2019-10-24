import random

nombre = input("Por favor digita el nombre del jugador: ")
nombre = nombre.upper()
usuario = []
computador = []
def user():
    return usuario
def pc():
    return computador

def resUser(res):
    res += res
    return res

def list_cartas():
    valor = ["A", "2", "3", "4", "5", "6", "7", "8", "9" , "10", "J", "Q", "K"]
    figura = ["c", "p", "d", "t"]
    carta = random.choice(valor) + random.choice(figura)
    return carta

def turno(t):
    if t == "user":
        if user() == []:
            user().append(list_cartas ())
            user().append(list_cartas ())
        else:
            user().append(list_cartas ())
        return user()
    else:
        if pc() == []:
            pc().append(list_cartas ())
            pc().append(list_cartas ())
        else:
            pc().append(list_cartas ())
        return pc()
        

def suma(res, inicio, t):
    if t == "user":
        for i in range(inicio, len(user())):
            if user()[i][0] in ["J", "Q", "K"]:
                res += 10
            elif user()[i][0] in ["A"]:
                res += int(input("Que valor desea 1 0 11 ?"))
            elif user()[i][0] == "1" and user()[i][1] == "0":
                res += 10
            else:
                res += int(user()[i][0])
        return res
    elif t == "maquina":
        res
        for i in range(inicio, len(pc())):
            if pc()[i][0] in ["J", "Q", "K"]:
                res += 10
                #print("primero" + str(res2))
            elif pc()[i][0] in ["A"]:
                des = random.choice([1, 11])
                res += des
                #print("segundo" + str(res2))
            elif pc()[i][0] in ["1"] and pc()[i][1] in["0"]:
                res += 10
            else:
                #print(pc()[i][0])
                res += int(pc()[i][0])
                #print("tercero" + str(res2))
        return res
                   
def validarGanador(numU, numC, userP, maqP):
    if (numU > numC and numU <= 21) or (numU<= 21 and numC > 21) :
        print("El ganador es "+ nombre + " con : " + str(numU) + " contra : " + str(numC) + " de la MAQUINA")
        userP += 1
    elif (numC > numU and numC <= 21) or (numC<= 21 and numU > 21) :
        print("El ganador es la MAQUINA con : " + str(numC) + " contra : " + str(numU) + " de "+ nombre + " ")
        maqP += 1
    elif numU == numC:
        print ("Empatados")
        userP +=1
        maqP +1
    
    del user()[:]
    del pc()[:]
    return userP, maqP
