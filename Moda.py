#---- Moda -----#
print ("Datos: ")
data=[1,5,6,1,4,3,8,7,8,1]

print (data)

repetir = 0                                                                         
for i in data:                                                                              
    aparece = data.count(i)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                       
                                                                                         
moda = []                                                                               
for i in data:                                                                              
    aparece = data.count(i)                                                             
    if aparece == repetir and i not in moda:                                   
        moda.append(i)                                                                  
                                                                                         
print ("moda:", moda)