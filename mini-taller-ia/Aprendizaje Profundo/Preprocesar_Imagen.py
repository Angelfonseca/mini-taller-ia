from PIL import Image
import numpy as np
import pandas as pd 
import sys
np.set_printoptions(threshold=sys.maxsize)

# Abrir imagen a color y convertirla a niveles de gris
image = Image.open('C:/Users/quelo/OneDrive/Desktop/Taller_IA/Taller_IA/Aprendizaje Profundo/Datos/large.jpeg').convert("L")

# Tamaño de la imagen
print(image.size)

# Rescalar la imagen a 32 x 32
image = image.resize((32,32))
image.save("C:/Users/quelo/OneDrive/Desktop/Taller_IA/Taller_IA/Aprendizaje Profundo/Datos/imagen4.jpg", "JPEG", optimize=True)

# tamaño de la imagen
print(image.size)

# Crear un arreglo con la imágen
arr = np.asarray(image).reshape(1024)

# Imprimir la forma del arreglo 
print(arr.shape)
# Imprimir el arreglo 
print(arr)

# convert array into dataframe 
df = pd.DataFrame(arr) 
  
# save the dataframe as a csv file 
df.to_csv("C:/Users/quelo/OneDrive/Desktop/Taller_IA/Taller_IA/Aprendizaje Profundo/Datos/datos_1.csv")

