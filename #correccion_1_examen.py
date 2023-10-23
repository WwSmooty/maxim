#correccion_1_examen
'''
#Pan viejo
cantidad=float(input())
pan=cantidad*25.49
descuento=(25.49/100)*60
descuentot= descuento*cantidad
print(pan)
print(descuento)
print(descuentot)

#Estaciones del año
mes=int(input())
dia=int(input())

if mes==4 or mes ==5:
    print('primavera')
if mes==7 or mes==8:
    print('verano')
if mes==10 or mes==11:
    print('otoño')
if mes==1 or mes==2:
    print('invierno')

if mes==3 and dia>=20:
    print('primavera')
if mes==3 and dia<=19:
    print('invierno')
if mes==12 and dia>=21:
    print('invierno')
if mes==12 and dia<=20:
    print('otoño')
if mes==6 and dia>=21:
    print('verano')
if mes==6 and dia<=20:
    print('primavera')
if mes==9 and dia>=22:
    print('otoño')
if mes==9 and dia<=21:
    print('verano')


#Regresando cambiio
recibido=int(input())
total=int(input())
cambio=recibido-total

aux=cambio%10
diez=cambio//10

cambio=diez
aux=cambio%5
cinco=cambio//5

cambio=cinco
aux=cambio%2
dos=cambio//2

cambio=dos
uno=cambio
print(diez,'-$10') 
print(diez,'-$5') 
print(diez,'-$2') 
print(diez,'-$1')

#visitantes
n=int(input())
total=0
for i in range(n):
    edad=int(input())
    if 3<= edad<=12:
        total+=140.5
    elif edad>=65:
        total+=180.30
    elif edad<3:
        continue
    else:
        total+=230.99
print('{:.2f}'.format(total))
'''
#canguros
