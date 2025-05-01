from PilaTF import Pila
from ColaPI import ColaPI

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

c4 = ColaPI()
c4.acolar(1)
c4.acolar(2)
c4.acolar(5)

c3 = ColaPI()
c3.acolar(5)
c3.acolar(2)
c3.acolar(1)

print(son_inversas(c4, c3))  # Esto ahora debería imprimir: True
