class Naves:
    def __init__(self, nombre, largo, tripulacion, tripulantes):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.tripulantes = tripulantes
        
    def __str__(self):
        return "Nombre: " + self.nombre + "\nLargo: " + str(self.largo) + "\nTripulacion: " + str(self.tripulacion) + "\nTripulantes: " + str(self.tripulantes)
    
    def __repr__(self):
        return self.__str__()

class XWing(Naves):
    def __init__(self, nombre, largo, tripulacion, tripulantes):
        super().__init__(nombre, largo, tripulacion, tripulantes)

        
    def __str__(self):
        return super().__str__() 
    
    def __repr__(self):
        return self.__str__()

v1 = XWing("X-Wing", 12.5, 1, 1)

class EstrellaMortal(Naves):

    def __init__(self, nombre, largo, tripulacion, tripulantes):
        super().__init__(nombre, largo, tripulacion, tripulantes)
        
    def __str__(self):
        return super().__str__() 
    
    def __repr__(self):
        return self.__str__()

v2 = EstrellaMortal("Estrella Mortal", 100, 1000, 1000)  
class HalconMilenario(Naves):
    
    def __init__(self, nombre, largo, tripulacion, tripulantes):
        super().__init__(nombre, largo, tripulacion, tripulantes)
        
    def __str__(self):
        return super().__str__() 
    
    def __repr__(self):
        return self.__str__()

v3= HalconMilenario("Halcon Milenario", 1000, 1, 4)  
class AT_ST(Naves):
        
        def __init__(self, nombre, largo, tripulacion, tripulantes):
            super().__init__(nombre, largo, tripulacion, tripulantes)
            
        def __str__(self):
            return super().__str__() 
        
        def __repr__(self):
            return self.__str__()
v4 = AT_ST("AT-ST", 20, 1, 1)   
class Maria(Naves):
        
        def __init__(self, nombre, largo, tripulacion, tripulantes):
            super().__init__(nombre, largo, tripulacion, tripulantes)
            
        def __str__(self):
            return super().__str__() 
        
        def __repr__(self):
            return self.__str__()
v5= Maria("Maria", 167, 6, 8)
class Andrea(Naves):
            
            def __init__(self, nombre, largo, tripulacion, tripulantes):
                super().__init__(nombre, largo, tripulacion, tripulantes)
                
            def __str__(self):
                return super().__str__() 
            
            def __repr__(self):
                return self.__str__()
            
v6 = Andrea("Andrea", 256, 4, 2)
class NavesEstelares:

    def __init__(self):
        self.naves = []
        
    def agregarNave(self, nave):
        self.naves.append(nave)
        
    def __str__(self):
        return str(self.naves)
    
    def __repr__(self):
        return self.__str__()

#print('NOMBRES ORDENADOS DE MANERA ASCENDENTE')
def ordenarNombre(naves):
    naves.sort(key=lambda nave: nave.nombre)
    print(naves)



#print('LARGO ORDENADOS DE MANERA DESCENDENTE')

def ordenarLargo(naves):
    naves.sort(key=lambda nave: nave.largo, reverse=True)
    print(naves)


#print('DATOS DE LAS NAVE HALCON MILENARIO Y ESTRELLA MORTAL')
def obtenerDatos(naves):
    for nave in naves:
        if nave.nombre == "Halcon Milenario":
            print(nave)
        if nave.nombre == "Estrella Mortal":
            print(nave)



#print('LAS 5 NAVE CON MAS TRIPULANTES')
def obtenerTripulantes(naves):
    naves.sort(key=lambda nave: nave.tripulantes, reverse=True)
    print(naves[:5])


#print('LA NAVE QUE REQUIERE MAS TRIPULANTES')
def obtenerNave(naves):
    naves.sort(key=lambda nave: nave.tripulantes, reverse=True)
    print(naves[0])


#print('LAS NAVE QUE EMPIEZAN POR AT')
def obtenerNaveAT(naves):
    for nave in naves:
        if nave.nombre.startswith("AT"):
            print(nave)


#print('LAS NAVE QUE PUEDEN LLEVAR 6 O MAS TRIPULANTES')
def obtenerNaveTripulantes(naves):
    for nave in naves:
        if nave.tripulantes >= 6:
            print(nave)


#print('LAS NAVE MAS PEQUEÑA Y MAS GRANDE')
def obtenerNavePequeña(naves):
    naves.sort(key=lambda nave: nave.largo)
    print(naves[0])


def obtenerNaveGrande(naves):
    naves.sort(key=lambda nave: nave.largo, reverse=True)
    print(naves[0])




    