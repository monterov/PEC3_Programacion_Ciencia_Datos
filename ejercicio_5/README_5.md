### Ejercicio 5.1 

Lo primero que debéis hacer es calcular el tiempo base de descarga, es decir, cuánto tarda el proceso en completarse de manera secuencial para las `n=50` imágenes.
Este valor servirá como referencia para poder comparar posteriormente con otras implementaciones.

Tendréis que implementar una función que recorra la lista de URLs y descargue todas las imágenes una a una, llamando a la función `download_image(url, idx)` para cada elemento.
Durante el proceso, debéis medir y mostrar el tiempo total de ejecución, de forma que se pueda conocer cuánto tarda el proceso secuencial completo.

**Nota:**

Antes de comenzar la descarga, asegurad que existe la carpeta donde se almacenarán las imágenes (por ejemplo, imgs/).
Para ello, se recomienda utilizar la función `os.makedirs()` con el parámetro `exist_ok=True`, que permite crear la carpeta automáticamente en caso de que no exista.

#### Error 

![Error_fs_11](pantallazo_15.png)

**Solución**

Importar from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

Durante la ejecución de las pruebas de descarga, se muestra esto: 

![Salida_1](pantallazo_16.png)

La salida tiene mucho ruído y es de la línea del código de la función download_image, así que no la voy a tocar y dejo la salida tal cual.




https://docs.python.org/es/3/library/concurrent.futures.html
https://docs.python.org/es/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor
https://youtu.be/SyJYiH9EcOk?si=xroG6ITI7oeQFiya
https://youtu.be/fU_WlPMQPZU?si=ytCvS7NG30NgtKo1
