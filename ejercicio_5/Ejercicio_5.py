import requests

def get_image_urls(num: int = 50) -> list[str]:
    """
    Fetches a list of random image URLs from the API.

    Args:
        num (int): Number of image URLs to retrieve.

    Returns:
        list[str]: A list containing the image URLs.
    """
    api_url = f"https://picsum.photos/v2/list?page=1&limit={num}"
    response = requests.get(api_url)
    return [item["download_url"] for item in response.json()]

import os

def download_image(url: str, idx: int) -> None:
    """
    Downloads a single image from a given URL and 
    saves it with a unique index.

    Args:
        url (str): The URL of the image to download.
        idx (int): The index used to create a unique filename.
    """
    filename = os.path.join("imgs", f"image_{idx}.jpg")
    try:
        r = requests.get(url)
        with open(filename, "wb") as f:
            f.write(r.content)
        print(f"Saved: {filename}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_image(url: str, idx: int, out_dir: str) -> None:
    """
    Downloads a single image from a given URL and saves it in out_dir.

    Args:
        url (str): Image URL.
        idx (int): Index used to create a unique filename.
        out_dir (str): Output directory where the image will be saved.
    """
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f"image_{idx}.jpg")

    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(filename, "wb") as f:
            f.write(r.content)
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Descarga secuencial de 50 imágenes (tiempo base)
descarga_imagenes(50)

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Función versión multithreading

def descarga_threads(urls: list[str], num_threads: int) -> float:

    os.makedirs("imgs_threads", exist_ok=True) # Nos aseguramos que existe la carpeta destino

# Iniciamos el temporizador
    inicio = time.perf_counter()

# Usamos la clase ThreadPoolExecutor para la ejecución paralela de tareas
  
    with ThreadPoolExecutor(max_workers=num_threads) as executor: 
        for idx, url in enumerate(urls):
            executor.submit(download_image, url, idx)

    return time.perf_counter() - inicio 

# Función versión multiprocessing

def descarga_procesos(urls: list[str], num_procesos: int) -> float:
    
    os.makedirs("imgs_procs", exist_ok=True) # Nos aseguramos que existe la carpeta destino

    # Iniciamos el temporizador

    inicio = time.perf_counter()

    # Usamos la clase ProcessPoolExecutor para hacer el paralelismo basado en procesos

    with ProcessPoolExecutor(max_workers=num_procesos) as executor:
        for idx, url in enumerate(urls):
            executor.submit(download_image, url, idx)
            
    return time.perf_counter() - inicio

# Marcamos 50 imágenes como fijo para la comparativa

urls = get_image_urls(50)

# Creamos las listas para almacenar las métricas
tiempos_threads = []
tiempos_procesos = []

# Hacemos test para ir probando los workers del 1 al 10 

for n in range(1, 11):
    t_thr = descarga_threads(urls, n)
    t_pro = descarga_procesos(urls, n)

    tiempos_threads.append(t_thr)
    tiempos_procesos.append(t_pro)

# Mostramos los resultados

print("\nResumen de los resultados:")
print("Threads :", [round(t, 4) for t in tiempos_threads])
print("Procesos:", [round(t, 4) for t in tiempos_procesos])

# Gráfica con los resultados

plt.figure()
plt.plot(range(1, 11), tiempos_threads, marker="o", label="Threads")
plt.plot(range(1, 11), tiempos_procesos, marker="o", label="Procesos")
plt.xlabel("Número de workers")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparativa threads vs procesos (50 imágenes)")
plt.legend()
plt.show()



