# Conversor de Imágenes
Este conversor de imágenes es una herramienta CLI que
tiene la finalidad de convertir imágenes de varios tipos
a un tipo en específico (Por ejemplo, WEBP y PNG a JPEG)

### Modo de uso
Para que esta aplicación funcione, debes establecer la
ruta de los archivos que deseas convertir y un destino
en donde quieras que los archivos convertidos sean guardados.

Para esto, debes editar el archivo ***.envExample*** y
borrar la palabra "Example" del archivo.

```.env py
INPUT_DIRECTORY='C:\\TU\\RUTA\\DE\\DIRECTORIO\\DE\\ENTRADA'

OUTPUT_DIRECTORY='C:\\TU\\RUTA\\DE\\DIRECTORIO\\DE\\SALIDA'
```
Luego abre Powershell o tu terminal favorita y crea un entorno virtual.

```bash
python -m env venv
```

Luego inicia el entorno virtual con:

```bash
./venv/Scripts/activate
```

Y cuando estés dentro del entorno virtual utiliza
```py
python -m pip install -r requirements.txt
```
Y ejecutar el archivo ***image_converter.py*** ubicado en ***./src/image_converter.py***

OJO
Si usas Windows debes de utilizar sí o sí dos backslashes (//) 
Con el fin de que el programa funcione y no detecte un error de caracter desconocido.