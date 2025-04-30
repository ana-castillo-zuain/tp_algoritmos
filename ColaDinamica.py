class Nodo:

    def __init__(self):
      self.sig = None
      self.info = None

class ColaDinamica:
    
    def __init__(self):
     self.primero = None
     self.ultimo = None

    def acolar(self, x):
       aux = Nodo()
       aux.info = x
       aux.sig = None

       #Si la cola no está vacía
       if self.ultimo != None:
          self.ultimo.sig = aux

       self.ultimo = aux

       #Si la cola estaba vacía
       if self.primero == None:
          self.primero = self.ultimo


    def desacolar(self):
       self.primero = self.primero.sig

       #Si la cola queda vacía
       if self.primero == None:
          self.ultimo = None

    def colaVacia(self):
       return (self.ultimo == None)
    
    def primerElemento(self):
        return self.primero.info

