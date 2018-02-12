#----- Promedio -----#

valores=[1,5,6,1,4,3,8,7,8,1]

def promedio(valores):
    sumaParcial=0
    for valor in valores:
        sumaParcial+=valor
        cantidadValores = len(valores)
        
    return sumaParcial/float(cantidadValores)

print(promedio(valores))