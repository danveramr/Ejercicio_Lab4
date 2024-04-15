import random
import math
import numpy as np

temperatura = 10
enfriamiento = 0.8
lim_s = [5]   
lim_i = [-5]  

def funcion(X):
    x=X[0]
    #f = x**4+3*x**3+2*x**2-1
    f = x**2-3*x-8
    return f

estado_inicial=np.zeros((1))
for v in range(1):
    estado_inicial[v] = random.uniform(lim_i[v],lim_s[v])
      
solucion_actual = estado_inicial
mejor_sol = estado_inicial
f_min = funcion(mejor_sol)
temp_actual = temperatura 
  
for i in range(100):
    for j in range(100):
  
       
        
        posible_sol = solucion_actual*temp_actual
        E = abs(posible_sol - f_min)

        if posible_sol > f_min:
            proba = math.exp(-E/temp_actual)
            if random.random()<proba:
                bool = True
            else:
                bool= False
        else:
            bool = True
            
        if bool == True:
            mejor_sol = solucion_actual
            f_min = funcion(mejor_sol)
    
    temp_actual = temp_actual * enfriamiento

print("\nValor mínimo de la función: {}".format(f_min))