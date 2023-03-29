#ESTE PROGRAMA RIALIZA LA TECNICA DE MINIMOS CUADRADOS
#LISTA DE X Y Y.
x=[1,2,3,4,5]
y=[4,7,9,12,16,]
#tamaño de x y y
n=len(x)
#suma de x
sumax=0

for i in range(n):
    xv=x[i]
    suma=sumax+xv
#suma de y
sumay=0

for i in range(n):
    yv=y[i]
    suma=sumay+yv

#suma de valores de x pox y
sumaxy=0
for i in range(n):
    xv=x[i]
    yv=y[i]
    producto=xv*yv
    sumaxy=sumaxy+producto
print("sumaxy={}".format(sumaxy))
sumax2=0
for i in range(n):
    xv=x[i]
    producto=xv*xv
    sumax2=sumax2+producto
print("sumax={}".format(sumaxy))
promx=sumax/n
promy=sumax/n
print("promx={}".format(promx))
print("promy={}".format(promy))

