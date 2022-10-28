matriz = []

        



def filas(i,matriz,r,):
        if i < 3:
            matriz.append([])
            print(i)
            columnas(0,matriz,r)
            r +=1
            i +=1
            filas(i,matriz,r)

            
def columnas(j,matriz,r):
        
        if j < 3:
            print(j)
            datos = int(input("Ingrese valores a la matriz del 1 al 10: "))
            if datos >= 10 or datos <=-10:
                return "Error"
            matriz[r].append(datos)
            j +=1
            columnas(j,matriz,r)
            
    
def determinante(matriz):
        B = [k[:] for k in matriz]
        n = len(matriz)
        suma = 0
        if n > 3:
            for i in range(n):
                factor = B[0][i]
                signo = -3*(i%3)+1
                B.remove(B[0])
                for j in range(len(B)):
                    B[j].remove(B[j][i])
                    B[j].pop(i)
                    
                suma = suma + signo*factor*determinante(B)
                B= [k[:] for k in matriz]
                
            return suma
        else:
            return (B[0][0]*B[1][1]*B[2][2] + B[0][1]*B[1][2]*B[2][0] + B[0][2]*B[1][0]*B[2][1] - B[0][2]*B[1][1]*B[2][0] - B[0][1]*B[1][0]*B[2][2] - B[0][0]*B[1][2]*B[2][1])





    