class ColaPI:
    def __init__(self): 
        self.elementos = []
        self.index = 0
    
    def acolar(self, datos): 
        self.elementos.append(datos) 
        self.index += 1
        return datos 
    
    def desacolar(self): 
        for i in range (self.index - 1):
            self.elementos[i] = self.elementos[i +1]

        self.index -= 1
        return self.elementos.pop()
        
    def primero(self): 
        return self.elementos[0]
        
    def colaVacia(self): 
        return (self.index == 0)