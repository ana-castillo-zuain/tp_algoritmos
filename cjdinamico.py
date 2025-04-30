import random

class Nodo:

    def __init__(self):
      self.sig = None
      self.info = None


class ConjuntoDinamico:
   
   def __init__(self):
    self.primero = None
    self.cantidad = 0
        
   def agregar(self, x):
        if not self.pertenece(x):
            nuevo = Nodo()
            nuevo.info = x
            nuevo.sig = self.primero
            self.primero = nuevo
            self.cantidad += 1
    
   def pertenece(self, x):
       viajero = self.primero

       while (viajero!= None and viajero.info != x):
          viajero = viajero.sig

       return(viajero != None)

   def sacar(self, x):
    if self.primero is None:
        print('El conjunto está vacío')
        return

    if self.primero.info == x:
        self.primero = self.primero.sig
        self.cantidad -= 1  
    else:
        viajero = self.primero
        while (viajero.sig != None and viajero.sig.info != x):
            viajero = viajero.sig

        if viajero.sig is None:
            print('Objeto no pertenece al conjunto')
        else:
            viajero.sig = viajero.sig.sig
            self.cantidad -= 1


   def elegir(self):
    if self.cantidad == 0:
        print('El conjunto está vacío')

    num = random.randint(0, self.cantidad - 1)
    viajero = self.primero

    for _ in range(num):
        if viajero is None:
            print('Error: índice fuera de rango')
            return None
        viajero = viajero.sig
    return viajero.info

   
   def ConjuntoVacio(self):
      if self.cantidad == 0:
         return True
      else: 
         return False
   
         
      

   

#cj = ConjuntoDinamico()
#c2 = ConjuntoDinamico()
#cj.agregar(10)
#cj.agregar(30)
#cj.agregar(50)
#cj.agregar(70)
#c2.sacar(9)
#cj.sacar(20)
#cj.sacar(10)
#cj.pertenece(10)
#cj.pertenece(30)
#cj.elegir()
#cj.elegir()