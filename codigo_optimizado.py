import time
import math
import numpy as np

def buscar_primos_numpy(limite):
    # Crear un array de booleanos (True = es primo)
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False  # 0 y 1 no son primos
    
    # Iterar solo hasta la raíz cuadrada de n
    raiz = int(math.sqrt(limite))
    
    for i in range(2, raiz + 1):
        if es_primo[i]:
            # Vectorización: Marcar todos los múltiplos de i como False
            es_primo[i*i : limite+1 : i] = False
            
    # Retornar los índices que quedaron como True
    return np.nonzero(es_primo)[0]

if __name__ == "__main__":
    print("--- Iniciando ejecución ---")  # Agrega esto para probar
    inicio = time.time()
    primos = buscar_primos_numpy(100000) 
    fin = time.time()
    
    print(f"Tiempo de ejecución (Optimizado): {fin - inicio:.6f} segundos")
    print(f"Total de primos encontrados: {len(primos)}")