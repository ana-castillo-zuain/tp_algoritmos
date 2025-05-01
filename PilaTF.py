class Pila:
    def __init__(self): 
        self.elementos = []
        self.index = 0
    
    def apilar(self, dato): 
        self.elementos.append(dato)
        self.index = self.index + 1
        return dato 
    
    def desapilar(self): 
        popi = self.elementos.pop()
        self.index -= 1
        return popi

        
    def tope(self): 
        return self.elementos[self.index - 1]
        
    def pilaVacia(self): 
        return (self.index == 0)
