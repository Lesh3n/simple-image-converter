from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

INPUT_DIRECTORY = os.getenv('INPUT_DIRECTORY')
OUTPUT_DIRECTORY = os.getenv('OUTPUT_DIRECTORY')


# Una tupla que contiene extensiones de archivos de imágen, se pueden agregar o eliminar las que se quieran.
image_file_extensions = ('.webp','.jpeg','.gif','.png','.tiff','.bmp','.svg','.jpg')

#Formato de conversión deseado. N.T NO EXISTE JPG!
desired_format_conversion = '.jpeg'

"""
Acá van las variables de entorno que se pueden modificar como en el ejemplo del archivo .env
para que establezan sus directorios allí. No es necesario modificar el código desde aquí.
"""

input_dir = INPUT_DIRECTORY
output_dir = OUTPUT_DIRECTORY

# Si el directorio de salida no existe (que será el caso) entonces crealo.
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#Crea un arreglo que contiene las imágenes dentro del directorio de entrada 
images_to_convert = os.listdir(input_dir)


if __name__ == '__main__':
    '''
    Recorre la lista que contiene las imágenes.
    '''
    for image in images_to_convert:
        if image.endswith(image_file_extensions): #Chequea si la imágen dentro de la lista termina con alguna extesión de la tupla.
            image_path = os.path.join(input_dir, image) #Hace la ruta del archivo juntando la ruta de entrada y el nombre del archivo.
            open_image = Image.open(image_path) #Abre la imágen
            if open_image != 'RGB': #Si la imágen no está en formato RGB, la transforma.
                open_image = open_image.convert('RGB')
            converted_file = os.path.splitext(image)[0] + desired_format_conversion #Agarra la imágen y le pone el formato deseado.
            output_path = os.path.join(output_dir, converted_file) #Crea la ruta de salida del archivo con el nuevo nombre de este mismo.
            open_image.save(output_path, format="jpeg") #Guarda la imágen en la ruta anterior y convierte el archivo al tipo deseado.
            
            print(f'Converted {image} to JPEG')

    print('Done! Conversion complete.')