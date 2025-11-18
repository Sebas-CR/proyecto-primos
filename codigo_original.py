import time

def es_primo_ineficiente(n):
    """Verifica si n es primo dividiendo por todos los números hasta n-1"""
    if n <= 1:
        return False
    for i in range(2, n):  # Ineficiencia: Itera hasta n
        if n % i == 0:
            return False
    return True

def buscar_primos_original(limite):
    primos = []
    for num in range(1, limite + 1):
        if es_primo_ineficiente(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    inicio = time.time()
    # Rango de 1 a 100,000
    primos = buscar_primos_original(20000) 
    fin = time.time()
    
    print(f"Tiempo de ejecución (Original): {fin - inicio:.4f} segundos")
    print(f"Total de primos encontrados: {len(primos)}")