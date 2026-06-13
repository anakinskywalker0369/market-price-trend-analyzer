import pandas as pd
import matplotlib.pyplot as plt
import os

def ejecutar_analisis():
    # Pedir el nombre del archivo
    nombre = input("Ingresa el nombre del archivo CSV: ")

    if not os.path.exists(nombre):
        print(f"Error: El archivo '{nombre}' no existe.")
        return

    try:
        # Carga el archivo (asumimos que usa coma como separador)
        df = pd.read_csv(nombre)
        
        # Limpieza: Convertimos las columnas a los formatos correctos
        # 'coerce' ayuda a que si hay un error, lo convierta en vacío (NaN) en lugar de romper
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
        
        # Eliminamos filas con datos faltantes o precios negativos
        df = df.dropna()
        df = df[df['precio'] > 0]
        
        # Ordenamos por fecha para el gráfico
        df = df.sort_values('fecha')

        # Visualización
        plt.figure(figsize=(10, 6))
        plt.plot(df['fecha'], df['precio'], marker='o', linestyle='-', color='teal')
        plt.title('Tendencia de Precios en el Tiempo')
        plt.xlabel('Fecha')
        plt.ylabel('Precio ($)')
        plt.grid(True)
        plt.show()

        print("¡Análisis completado con éxito!")
        print(df)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_analisis()