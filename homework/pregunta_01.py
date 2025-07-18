"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    lista_filas = []
    fila_temp = []


    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as archivo:
        lector = archivo.readlines()
    

    for linea in  lector[4:]:
          if linea.strip():  
              fila_temp.append(linea.strip())
          else:
              if fila_temp: 
                  lista_filas.append(" ".join(fila_temp))
                  fila_temp = []

    datos_procesados = []
    for fila in lista_filas:
          part = fila.split()
          id_cluster = int(part[0])
          total_palabras = int(part[1])
          porcentaje_palabras = float(part[2].replace(",", "."))
          palabras_clave = ( " ".join(part[3:]).replace(" ,", ",").replace(", ", ", ").strip("%").rstrip(".").strip())
          datos_procesados.append([id_cluster, total_palabras, porcentaje_palabras, palabras_clave])

    df= pd.DataFrame(datos_procesados, columns=[ "cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])

    return df

