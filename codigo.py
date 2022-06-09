""""Bimestral de Sistemas Práctica:
programa en Python para simular el lanzamiento de n dados, realizando la estadística de
 frecuencias de las veces que cayó cada cara, mediante un "histograma" horizontal:"""

import random

 # Input
veces=int(input("Digite la cantidad de veces que desea lanzar el dado: "))

 #Processing
cara1=0
cara2=0
cara3=0
cara4=0
cara5=0
cara6=0

sum=0
while sum<veces:
    ran=random.randint(1,6)
    sum=sum+1
    if ran==1:
        cara1=cara1+1
    elif ran==2:
        cara2=cara2+1
    elif ran==3:
        cara3=cara3+1
    elif ran==4:
        cara4=cara4+1
    elif ran==5:
        cara5=cara5+1
    elif ran==6:
        cara6=cara6+1

h="*"
cara1v=h*cara1
cara2v=h*cara2
cara3v=h*cara3
cara4v=h*cara4
cara5v=h*cara5
cara6v=h*cara6

#Output
print("Cara 1:", cara1v, cara1)    
print("Cara 2:", cara2v, cara2)
print("Cara 3:", cara3v, cara3)
print("Cara 4:", cara4v, cara4)
print("Cara 5:", cara5v, cara5)
print("Cara 6:", cara6v, cara6)
