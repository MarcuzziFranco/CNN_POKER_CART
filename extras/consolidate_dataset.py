import os
import shutil
import random

def consolidate_and_split_dataset(palo_folder, output_folder, split=(0.7, 0.2, 0.1)):
    """
    Consolida, mezcla y divide las imágenes de un palo en conjuntos de entrenamiento, validación y prueba.

    Args:
        palo_folder (str): Carpeta principal del palo (e.g., "As_trebol").
        output_folder (str): Carpeta base donde se guardarán los conjuntos.
        split (tuple): Proporciones para entrenamiento, validación y prueba (e.g., (0.7, 0.2, 0.1)).
    """
    # Crear carpetas de salida
    train_folder = os.path.join(output_folder, "train")
    val_folder = os.path.join(output_folder, "val")
    test_folder = os.path.join(output_folder, "test")

    for folder in [train_folder, val_folder, test_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Consolidar todas las imágenes en una lista
    all_images = []
    for filter_folder in os.listdir(palo_folder):
        filter_path = os.path.join(palo_folder, filter_folder)

        if os.path.isdir(filter_path):  # Verificar que sea una carpeta
            for image_file in os.listdir(filter_path):
                image_path = os.path.join(filter_path, image_file)
                if os.path.isfile(image_path):  # Verificar que sea un archivo
                    all_images.append(image_path)

    # Mezclar aleatoriamente las imágenes
    random.shuffle(all_images)

    # Dividir en entrenamiento, validación y prueba
    total_images = len(all_images)
    train_end = int(split[0] * total_images)
    val_end = train_end + int(split[1] * total_images)

    train_images = all_images[:train_end]
    val_images = all_images[train_end:val_end]
    test_images = all_images[val_end:]

    # Función para copiar imágenes con nombres únicos
    def save_images(images, folder, prefix):
        for idx, image_path in enumerate(images):
            new_name = f"{prefix}_{idx + 1:05d}.jpg"
            dest_path = os.path.join(folder, new_name)
            shutil.copy(image_path, dest_path)
            print(f"Copiada: {image_path} -> {dest_path}")

    # Guardar las imágenes en las carpetas correspondientes
    save_images(train_images, train_folder, "train")
    save_images(val_images, val_folder, "val")
    save_images(test_images, test_folder, "test")

    print("Consolidación y división completa:")
    print(f"- Entrenamiento: {len(train_images)} imágenes en {train_folder}")
    print(f"- Validación: {len(val_images)} imágenes en {val_folder}")
    print(f"- Prueba: {len(test_images)} imágenes en {test_folder}")

# Ejemplo de uso
palo_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol"  # Carpeta del palo específico
output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\As_trevol_dataset"
consolidate_and_split_dataset(palo_folder, output_folder, split=(0.7, 0.2, 0.1))