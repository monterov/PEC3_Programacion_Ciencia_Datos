## Ejercicio 2
En este ejercicio dispondréis de un conjunto de datos llamado music_dataset.csv, que contiene información sobre usuarios de una plataforma de música en línea. El fichero incluye variables como el país, la edad del usuario, el tipo de suscripción, el tiempo total de uso de la plataforma, un indicador que muestra si el usuario sigue activo o ha abandonado el servicio, etc.

El objetivo es analizar el rendimiento de dos estrategias distintas de lectura y procesamiento de datos para determinar cuál resulta más eficiente en términos de tiempo y recursos.


### Ejercicio 2.1 

Debéis implementar dos funciones que calculen el tiempo promedio de reproducción por tipo de suscripción (subscription_type). Tenéis la columna listening_time.

Implementación A: realizad la lectura del archivo de forma manual utilizando las funciones integradas de Python (open() y read()), procesando línea a línea los datos para calcular el promedio.

Implementación B: implementad la misma funcionalidad utilizando la librería pandas, aprovechando sus métodos (read_csv, groupby y mean).

Ambas funciones deben recibir únicamente el parámetro path: str, correspondiente a la ruta del fichero de datos. En ambos casos, no debe realizarse ningún tipo adicional de manipulación ni mostrar información por pantalla. Las funciones deberán únicamente devolver un diccionario con el resultado calculado.

#### Vamos a resolver

Lo primero es descargar el archivo de Drive y echarle un vistazo rápido a su estructura. Como siempre monto Drive y añado ruta de archivo. 

from google.colab import drive
drive.mount('/content/drive')
file_path = "/content/drive/My Drive/Colab Notebooks/Activity_3/data/music_dataset.csv"







![Comprobación funciones](Pantallazo_3.png)




#### Error

Aparece el primer error de código al llamar a la función. El error se producía al intentar acumular el timepo de escucha usando la instrucción "+=" sobre una clave del diccionario que no había sido incializada aún. 

*Línea del problema:*
sums[subscription] += listening_time

![Error al llamar a la función](Pantallazo_6.png)

Para resolverlo

Sustituyo la operación `+=` por el uso del método `get()`, inicializando el acumulador a 0.0 cuando el tipo de suscripción aparece por primera vez. 

### Referencias

*Explicación del método `get()` de los diccionarios en Python:*
https://thedataschools.com/python/diccionarios/get-metodo-diccionario.html
