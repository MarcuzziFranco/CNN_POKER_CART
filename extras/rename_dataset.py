import os

def rename_files_in_folder(folder_path, prefix):
    """
    Renombra todos los archivos en una carpeta con un prefijo y un índice numérico secuencial.

    Args:
        folder_path (str): Ruta a la carpeta que contiene los archivos a renombrar.
        prefix (str): Prefijo para los nombres de los archivos.

    """
    # Verificar si la carpeta existe
    if not os.path.exists(folder_path):
        print(f"La carpeta no existe: {folder_path}")
        return

    # Listar todos los archivos en la carpeta
    files = os.listdir(folder_path)
    files.sort()  # Ordenar para mantener consistencia en los nombres
    print(f"Renombrando {len(files)} archivos en la carpeta: {folder_path}")

    for idx, file_name in enumerate(files):
        # Obtener la extensión del archivo
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue  # Ignorar subcarpetas u otros elementos

        file_ext = os.path.splitext(file_name)[1]  # Extensión del archivo (e.g., .jpg, .npy)
        new_name = f"{prefix}_{idx + 1:05d}{file_ext}"  # Nuevo nombre (e.g., prefix_00001.jpg)
        new_path = os.path.join(folder_path, new_name)

        # Renombrar el archivo
        os.rename(file_path, new_path)
        print(f"Renombrado: {file_name} -> {new_name}")

    print(f"Renombrado completado en la carpeta: {folder_path}")

# Ejemplo de uso
folder_path = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\dataset\\As_trevol_dataset_normalizado\\test"
prefix = "as_trevol_test"
rename_files_in_folder(folder_path, prefix)