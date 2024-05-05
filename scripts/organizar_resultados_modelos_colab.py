import os
import shutil

def organizar_archivos_por_modelo(ruta_origen, prefijo_carpeta="", mover = False):
    """Organiza archivos por modelo en carpetas separadas."""
    
    # Obtener la lista de archivos en la ruta de origen
    # archivos = os.listdir(ruta_origen)
    archivos = [archivo for archivo in os.listdir(ruta_origen) if not archivo.startswith("~$")]
    
    # Iterar sobre los archivos
    for archivo in archivos:
        # Verificar si es un archivo
        if os.path.isfile(os.path.join(ruta_origen, archivo)):
            print(archivo)
            # Obtener el nombre del modelo del archivo
            nombre_modelo = archivo.replace("Modelo_", "").replace(".h5", "").replace(".xlsx", "").replace("History_", "")
            # Crear el nombre de la carpeta del modelo
            nombre_carpeta_modelo = f"{prefijo_carpeta}{nombre_modelo}"
            # Crear la ruta de la carpeta del modelo
            ruta_carpeta_modelo = os.path.join(ruta_origen, nombre_carpeta_modelo)

            print(f"Modelo: {nombre_carpeta_modelo}")

            if mover:
                print("Moviendo archivos")
                # Crear la carpeta si no existe
                if not os.path.exists(ruta_carpeta_modelo):
                    os.makedirs(ruta_carpeta_modelo)
                # Mover el archivo a la carpeta del modelo
                shutil.move(os.path.join(ruta_origen, archivo), os.path.join(ruta_carpeta_modelo, archivo))

# Ejemplo de uso
ruta_origen = r'G:/Mi unidad/Maestria/Tesis/Bayesian_NN/Modelos_Colab/'
prefijo_carpeta = "pesos_"  # Puedes cambiar esto según lo necesites
organizar_archivos_por_modelo(ruta_origen, prefijo_carpeta, mover = True)