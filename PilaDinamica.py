

class Nodo:

    def __init__(self):
      self.sig = None
      self.info = None


class PilaDinamica:
   
   def __init__(self):
    self.primero = None
        
   def apilar(self, x):
        aux = Nodo()
        aux.info = x
        aux.sig = self.primero
        self.primero = aux
    
   def desapilar(self):
       self.primero = self.primero.sig

   def pilaVacia(self):
       return (self.primero == None)
    
   def tope(self):
       return self.primero.info


    

    



