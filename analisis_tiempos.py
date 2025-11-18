import cProfile
import pstats
import time
import matplotlib.pyplot as plt
from codigo_original import buscar_primos_original
from codigo_optimizado import buscar_primos_numpy

def correr_profiling():
    print("--- Iniciando Profiling ---")
    
    # NOTA: Reducimos el límite del original para el profiling 
    # para que no tarde una eternidad, pero proyectamos la gráfica.
    LIMIT_ORIGINAL = 10000 
    LIMIT_OPTIMIZADO = 100000

    # 1. Profiling del código original
    print(f"Ejecutando Original (hasta {LIMIT_ORIGINAL})...")
    profiler = cProfile.Profile()
    profiler.enable()
    buscar_primos_original(LIMIT_ORIGINAL)
    profiler.disable()
    
    # Guardar estadísticas
    with open("profiling_original.txt", "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats('cumtime')
        stats.print_stats()

    # 2. Medición simple de tiempos para comparar (Escala igualada a 100k)
    # Medimos tiempo real
    start = time.time()
    buscar_primos_original(10000) # Muestra pequeña
    t_original_10k = time.time() - start
    # Proyección lineal simple para 100k (estimada)
    t_original_est = t_original_10k * 10 

    start = time.time()
    buscar_primos_numpy(100000)
    t_optimizado = time.time() - start

    print(f"Tiempo Original (Estimado 100k): {t_original_est:.4f} s")
    print(f"Tiempo Optimizado (Real 100k): {t_optimizado:.4f} s")

    return t_original_est, t_optimizado

def generar_graficos(t_orig, t_opt):
    etiquetas = ['Original (Est.)', 'Optimizado (NumPy)']
    tiempos = [t_orig, t_opt]
    
    plt.figure(figsize=(10, 6))
    barras = plt.bar(etiquetas, tiempos, color=['red', 'green'])
    
    plt.ylabel('Tiempo en Segundos (Menos es mejor)')
    plt.title('Comparativa de Rendimiento: Búsqueda de Primos (N=100,000)')
    
    # Añadi el valor encima de las barras
    for bar in barras:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.5f}s', ha='center', va='bottom')

    plt.savefig('comparativa_tiempos.png')
    print("Gráfico guardado como 'comparativa_tiempos.png'")
    plt.show()

if __name__ == "__main__":
    t_orig, t_opt = correr_profiling()
    generar_graficos(t_orig, t_opt)