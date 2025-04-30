class NodoABB:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoABB(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = NodoABB(dato)
            else:
                self._insertar(nodo.izq, dato)
        elif dato > nodo.dato:
            if nodo.der is None:
                nodo.der = NodoABB(dato)
            else:
                self._insertar(nodo.der, dato)

def esta_en_abb_iterativo(nodo, valor):
    actual = nodo
    while actual:
        if actual.dato == valor:
            return True
        elif valor < actual.dato:
            actual = actual.izq
        else:
            actual = actual.der
    return False

def es_hoja(nodo, valor):
    if nodo is None:
        return False
    if nodo.dato == valor:
        return nodo.izq is None and nodo.der is None
    elif valor < nodo.dato:
        return es_hoja(nodo.izq, valor)
    else:
        return es_hoja(nodo.der, valor)

def profundidad(nodo, valor, nivel=0):
    if nodo is None:
        return -1
    if nodo.dato == valor:
        return nivel
    elif valor < nodo.dato:
        return profundidad(nodo.izq, valor, nivel + 1)
    else:
        return profundidad(nodo.der, valor, nivel + 1)

def menor_elemento(nodo):
    actual = nodo
    while actual and actual.izq:
        actual = actual.izq
    return actual.dato if actual else None

def contar_elementos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_elementos(nodo.izq) + contar_elementos(nodo.der)

