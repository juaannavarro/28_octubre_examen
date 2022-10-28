class Polinomio:
    def __init__(self):
        self.poli = []
    def agregar(self, coef, exp):
        self.poli.append([coef, exp])
    def mostrar(self):
        for i in range(len(self.poli)):
            print(self.poli[i][0], "x^", self.poli[i][1], " + ", end="")
        print()
    def restar(self, poli2):
        poli3= Polinomio()
        i = 0
        j = 0
        while i < len(self.poli) and j < len(poli2.poli):
            if self.poli[i][1] == poli2.poli[j][1]:
                poli3.agregar(self.poli[i][0] - poli2.poli[j][0], self.poli[i][1])
                i += 1
                j += 1
            elif self.poli[i][1] > poli2.poli[j][1]:
                poli3.agregar(self.poli[i][0], self.poli[i][1])
                i += 1
            else:
                poli3.agregar(poli2.poli[j][0], poli2.poli[j][1])
                j += 1
                
        while i < len(self.poli):
            poli3.agregar(self.poli[i][0], self.poli[i][1])
            i += 1
        while j < len(poli2.poli):
            poli3.agregar(poli2.poli[j][0], poli2.poli[j][1])
            j += 1
        return poli3
    def division(self, poli2):
        poli3 = Polinomio()
        i = 0
        j = 0
        while i < len(self.poli) and j < len(poli2.poli):
            if self.poli[i][1] == poli2.poli[j][1]:
                poli3.agregar(self.poli[i][0] / poli2.poli[j][0], self.poli[i][1])
                i += 1
                j += 1
            elif self.poli[i][1] > poli2.poli[j][1]:
                poli3.agregar(self.poli[i][0], self.poli[i][1])
                i += 1
            else:
                poli3.agregar(poli2.poli[j][0], poli2.poli[j][1])
                j += 1
        while i < len(self.poli):
            poli3.agregar(self.poli[i][0], self.poli[i][1])
            i += 1
        while j < len(poli2.poli):
            poli3.agregar(poli2.poli[j][0], poli2.poli[j][1])
            j += 1
        return poli3
    
    def eliminar(self, termino):
        for i in range(len(self.poli)):
            if self.poli[i][1] == termino:
                self.poli.remove(self.poli[i])
                break
            
    def existe(self, termino):
        for i in range(len(self.poli)):
            if self.poli[i][1] == termino:
                return True
        return False