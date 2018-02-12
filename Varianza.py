#----- Varianza -----#
def print_g(g):
    for grade in g:
        print (grade)

def suma(g):
    total = 0
    for grade in g: 
        total += grade
    return total
    
def g_a(g):
    sum = suma(g)
    a = float(sum) / len(g)
    return a

def t_varianza(s, a):
    r = 0
    for data in s:
        r += (a - float(data))**2
    varianza = float(r)/len(g)
    return varianza

g = [1, 5, 6, 1, 4, 3, 8, 7, 8, 1] 
print (t_varianza(g, g_a(g)))