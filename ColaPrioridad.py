class ColaPrioridad:
    
    class Elemento:
        def __init__(self):
            self.valor = 0
            self.prioridad = 0

    def __init__(self): 
        self.elementos = []
        self.index = 0
    
    def acolarPrioridad(self, x, prioridad): 
        i = self.index
        if self.index > 0:
            self.elementos.append(self.elementos [self.index - 1])

            while (i>0 and self.elementos[i -1].prioridad < prioridad): #Hacemos la operación de corrimiento hacia la derecha para dejar el hueco
                self.elementos[i] = self.elementos[i - 1]
                i-= 1
            
            self.elementos[i] = self.Elemento(°)
            self.elementos[i].valor = x
            self.elementos[i].prioridad = prioridad
        else:
            elemento = self.Elemento()
            elemento.valor = x
            elemento.prioridad = prioridad
            self.elementos.append(elemento)


        self.index += 1
        return x 
    
    def desacolar(self): 
        self.index -= 1
        
    def primero(self): 
        return self.elementos[self.index - 1].valor
        
    def prioridad(self):
        return self.elementos[self.index - 1].prioridad
    
    def colaVacia(self): 
        return (self.index == 0)