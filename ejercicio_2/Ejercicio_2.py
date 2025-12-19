from google.colab import drive
drive.mount('/content/drive')
file_path = "/content/drive/My Drive/Colab Notebooks/Activity_3/data/music_dataset.csv"

# Ruta local al fichero de datos 
file_path = "data/music_dataset.csv"

# Leemos el archivo y comprobamos las columnas
with open(file_path, "r", encoding="utf-8") as f:
    columnas = f.readline().strip().split(",")

print(columnas)


# Creamos función implementación A

def tiempo_promedio_suscripcion_manual(path: str) -> dict:
    """
    Calcula el promedio de listening_time por subscription_type leyendo el CSV de forma manual

    Args:
        path (str): Ruta al fichero CSV.

    Returns:
        dict: {subscription_type: promedio_listening_time}
    """
    # Diccionarios para acumular la suma de tiempos y número de registros por suscriptores

    sums = {}
    counts = {}

    # Abrimos el archivo y leemos la cabecera, localizando las columnas que necesitamos

    with open(path, "r", encoding="utf-8") as f: 
        header = f.readline().strip().split(",")
        sub_idx = header.index("subscription_type")
        time_idx = header.index("listening_time")

    # Procesamos el archivo línea a línea

        for line in f: 
            parts = line.strip().split(",")
            subscription = parts[sub_idx]
            listening_time = float(parts[time_idx])

    # Acumulamos tiempo y contador por tipo de suscripción

            sums[subscription] = sums.get(subscription, 0.0) + listening_time
            counts[subscription] = counts.get(subscription, 0) + 1

    # Calculamos el promedio final por suscripción

    return {sub: (sums[sub] / counts[sub]) for sub in sums}   

# Creamos función implementación B

import pandas as pd

def tiempo_promedio_suscripcion_manual_pandas(path: str) -> dict:
    """
    Calcula el promedio de listening_time por subscription_type usando pandas.

    Args:
        path (str): Ruta al fichero CSV.

    Returns:
        dict: {subscription_type: promedio_listening_time}
    """ 

    # Leemos archivo y creamos Dataframe

    df = pd.read_csv(path) 
    result = df.groupby("subscription_type")["listening_time"].mean() # Agrupamos por tipo de suscripción y calculamos media de tiempo de escucha
    return result.to_dict()

# Analizamos implementaciones usando %timeit para la implementación A

%timeit tiempo_promedio_suscripcion_manual(file_path)
# Analizamos implementaciones usando %timeit para la implementación B

%timeit tiempo_promedio_suscripcion_manual_pandas(file_path)

!pip -q install line_profiler
%load_ext line_profiler

# Analizamos implementaciones usando %lprun para la implemtación A

%lprun -f tiempo_promedio_suscripcion_manual tiempo_promedio_suscripcion_manual(file_path)
# Analizamos implementaciones usando %lprun para la implemtación B

%lprun -f tiempo_promedio_suscripcion_manual_pandas tiempo_promedio_suscripcion_manual_pandas(file_path)
