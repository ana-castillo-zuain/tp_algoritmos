from PilaTF import Pila
from ColaPI import ColaPI
from ColaPrioridad import ColaPrioridad

#1
def copiar_pila(pila_origen):
    pila_copia = Pila()

    temp_list = []
    while not pila_origen.pilaVacia():
        temp_list.append(pila_origen.desapilar())

    for elem in reversed(temp_list):
        pila_origen.apilar(elem)
        pila_copia.apilar(elem)

    return pila_copia

def contar_elementos_pila(pila):
    return pila.index

def sumar_elementos_pila(pila):
    suma = 0
    pila_aux = copiar_pila(pila)
    while not pila_aux.pilaVacia():
        suma += pila_aux.desapilar()
    return suma

def promedio_pila(pila):
    if pila.pilaVacia():
        return None
    return sumar_elementos_pila(pila) / contar_elementos_pila(pila)

pi = Pila()
pi.apilar(2)
pi.apilar(3)
pi.apilar(4)

print(promedio_pila(pi))

#2
def elementos_finales(cola1, cola2):
    elem1 = None
    while not cola1.colaVacia():
        elem1 = cola1.desacolar()

    elem2 = None
    while not cola2.colaVacia():
        elem2 = cola2.desacolar()
    
    return elem2 == elem1

c1 = ColaPI()
c2 = ColaPI()
c1.acolar(1)
c2.acolar(2)
c1.acolar(2)
c2.acolar(3)
c1.acolar(5)
c2.acolar(4)

print(elementos_finales(c1,c2))

#3
def copiar(cola):
    copia = ColaPI()
    for i in range(cola.index):
        copia.acolar(cola.elementos[i])
    return copia


def invertir_cola(cola):
    copia = copiar(cola)
    inversa = ColaPI()
    pilaaux = Pila()

    while not copia.colaVacia():
        pilaaux.apilar(copia.desacolar())
    
    while not pilaaux.pilaVacia():
        inversa.acolar(pilaaux.desapilar())
    
    return inversa

def colas_iguales(c1, c2):
    if c1.index != c2.index:
        return False
    for i in range(c1.index):
        if c1.elementos[i] != c2.elementos[i]:
            return False
    return True

def son_inversas(c1, c2):
    return colas_iguales(invertir_cola(c1), c2)

#Ejemplo 1 -> True
c4 = ColaPI()
c4.acolar(1)
c4.acolar(2)
c4.acolar(5)

c3 = ColaPI()
c3.acolar(5)
c3.acolar(2)
c3.acolar(1)

print(son_inversas(c4, c3)) 

#Ejemplo 1 -> False

ca = ColaPI()
ca.acolar(1)
ca.acolar(2)
ca.acolar(5)

cb = ColaPI()
cb.acolar(6)
cb.acolar(2)
cb.acolar(1)

print(son_inversas(ca, cb)) 

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

#Opcion 1

Salas = {'PA' : 'Sala 1', 'PB' : 'Sala 2', 'JA' : 'Sala 3', 'JB': 'Sala 4',
         'MA': 'Sala 5', 'MB': 'Sala 6'}
Filas = {'PA' : ColaPrioridad(), 'PB' : ColaPrioridad(), 'JA' : ColaPrioridad(), 
         'JB': ColaPrioridad(), 'MA': ColaPrioridad(), 'MB': ColaPrioridad()}
Contadores = {'PA' : 1, 'PB' : 1, 'JA' : 1, 'JB': 1,
         'MA': 1, 'MB': 1}

def ingresar_turno(tipo, prioridad):
    ticket = f'{tipo}{Contadores[tipo]:03d}'
    Filas[tipo].acolarPrioridad(ticket,prioridad)
    Contadores[tipo] += 1
    print('Turno Ingresado ' + ticket)

def mostrar_turnos():
    print('\nTurnos Programados')
    for tipo, cola in Filas.items():
        print('\nTipo: ' + (tipo) + ' | Sala asignada: '+ (Salas[tipo]))
        while not cola.colaVacia():
            turno = cola.primero()
            print('Turno:'+ (turno))
            cola.desacolar()

ejemplos = [
        ("PA", 1), ("PA", 0), ("PA", 1),
        ("PB", 0), ("PB", 1), ("PB", 0),
        ("JA", 1), ("JA", 1), ("JA", 0),
        ("JB", 0), ("JB", 0), ("JB", 1),
        ("MA", 0), ("MA", 1), ("MA", 1),
        ("MB", 0), ("MB", 1), ("MB", 0),
    ]

for tipo, prioridad in ejemplos:
    ingresar_turno(tipo, prioridad)

mostrar_turnos()

