def Hanoi(discos, TorreOrigen =1, TorreAuxiliar=2, TorreDestino=3):
    if discos == 1:
        print ("Mover disco de la torre", TorreOrigen, "a la torre", TorreDestino)
    else:
        Hanoi(discos-1, TorreOrigen, TorreDestino, TorreAuxiliar)
        print("Mover disco de la torre", TorreOrigen, "a la torre", TorreDestino)
        Hanoi(discos-1, TorreAuxiliar, TorreOrigen, TorreDestino)
        
def jugarHanoi():
    discos = int(input("Ingrese la cantidad de discos: "))
    Hanoi(discos)
