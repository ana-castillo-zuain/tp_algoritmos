#EJERCICIO 4 -> Determinar si dos Colas con prioridad son idénticas.
from ColaPrioridad import ColaPrioridad

def colas_prioridad_iguales(cp1: ColaPrioridad, cp2: ColaPrioridad) -> bool:
    if cp1.index != cp2.index:
        return False

    for i in range(cp1.index):
        e1 = cp1.elementos[i]
        e2 = cp2.elementos[i]
        if e1.valor != e2.valor or e1.prioridad != e2.prioridad:
            return False

    return True

# #Ejemplo 1 -> False
cp1 = ColaPrioridad()
cp2 = ColaPrioridad()

# Primera cola: 
cp1.acolarPrioridad(10, 1)
cp1.acolarPrioridad(20, 3)
cp1.acolarPrioridad(30, 2)

# Segunda cola: 
cp2.acolarPrioridad(10, 1)
cp2.acolarPrioridad(20, 3)
cp2.acolarPrioridad(99, 2)  

#Ejemplo 2 -> True
cp3 = ColaPrioridad()
cp4 = ColaPrioridad()

# Primera cola: 
cp3.acolarPrioridad(10, 1)
cp3.acolarPrioridad(20, 3)
cp3.acolarPrioridad(30, 2)

# Segunda cola: 
cp4.acolarPrioridad(10, 1)
cp4.acolarPrioridad(20, 3)
cp4.acolarPrioridad(30, 2)

#Ejemplo 3 -> False

cp5 = ColaPrioridad()
cp6 = ColaPrioridad()

# Primera cola: 
cp5.acolarPrioridad(10, 1)
cp5.acolarPrioridad(20, 3)
cp5.acolarPrioridad(30, 2)

# Segunda cola: 
cp6.acolarPrioridad(10, 1)
cp6.acolarPrioridad(20, 3)
cp6.acolarPrioridad(2, 30)

#Ejemplo 3 -> False

cp7 = ColaPrioridad()
cp8 = ColaPrioridad()

# Primera cola: 
cp7.acolarPrioridad(10, 1)
cp7.acolarPrioridad(20, 3)
cp7.acolarPrioridad(30, 2)

# Segunda cola: 
cp8.acolarPrioridad(10, 1)
cp8.acolarPrioridad(20, 3)
cp8.acolarPrioridad(30, 2)
cp8.acolarPrioridad(40, 4)

# Comprobación
print("¿Son idénticas?: ", "Ejemplo 1: ",colas_prioridad_iguales(cp1, cp2), "Ejemplo 2: ", colas_prioridad_iguales(cp3, cp4), "Ejemplo 3: ", colas_prioridad_iguales(cp5, cp6),"Ejemplo 4: ", colas_prioridad_iguales(cp7, cp8))  


#EJERCICIO 5

from PilaTF import Pila

#Definimos la funcion, auxiliar: pila temporal donde guardamos los elementos no repetidos.
# vistos: conjunto (set) para registrar elementos que ya aparecieron.

def eliminar_duplicados_pila(pila: Pila):
    auxiliar = Pila()
    vistos = set()

#Recorremos la pila
#Sacamos uno por uno los elementos de la pila original (desde el tope).
#Si  no fue visto, lo apilamos en la auxiliar y lo registramos como "visto".
#Esto elimina duplicados conservando el primero que se agregó a la pila (es decir, el que está más abajo).

    while not pila.pilaVacia():
        dato = pila.tope()
        pila.desapilar()
        if dato not in vistos:
            vistos.add(dato)
            auxiliar.apilar(dato)

#Restauramos el orden original, Invertimos auxiliar usando otra pila restaurador, para dejar los elementos en orden original.
    restaurador = Pila()
    while not auxiliar.pilaVacia():
        dato = auxiliar.tope()
        auxiliar.desapilar()
        restaurador.apilar(dato)

#Volvemos a caragar la pila original
#Finalmente, vaciamos restaurador hacia la pila original. Ahora pila tiene:
#Elementos sin duplicados. En el mismo orden que originalmente ingresaron.

    while not restaurador.pilaVacia():
        dato = restaurador.tope()
        restaurador.desapilar()
        pila.apilar(dato)

# Ejemplo de uso
p = Pila()
for valor in [1, 2, 3, 2, 4, 3, 5]:
    p.apilar(valor)

eliminar_duplicados_pila(p)

# Mostrar resultado: 
while not p.pilaVacia():
    print(p.tope())
    p.desapilar()
