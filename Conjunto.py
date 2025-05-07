from random import randint

class Conjunto:
    def __init__(self): 
        self.elementos = []
        self.index = 0
    
    def pertenece(self, x):
        i = 0
        while(i < self.index and self.elementos [i]!= x):
            i +=1

        return (i < self.index) 
    
    def agregar(self, x): 
        if not self.pertenece(x):
            self.elementos.append(x)
            self.index += 1
        
    def sacar(self, x):
        i = 0

        while (i< self.index and self.elementos[i] != x):
            i+=1

        if i< self.index:
            self.elementos[i] = self.elementos[self.index - 1]
            self.index -= 1

    def elegir(self):
        i = randint(0, self.index - 1)
        return self.elementos[i]
    
    def conjuntoVacio(self): 
        return (self.index == 0)
    
