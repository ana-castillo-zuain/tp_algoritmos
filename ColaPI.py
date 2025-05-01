class ColaPI:
    def __init__(self): 
        self.elementos = []
        self.index = 0
    
    def acolar(self, datos): 
        self.elementos.append(datos) 
        self.index += 1
        return datos 
    
    def desacolar(self): 
        popi = self.elementos.pop(0)
        self.index -= 1
        return popi

        
    def primero(self): 
        return self.elementos[0]
        
    def colaVacia(self): 
        return (self.index == 0)