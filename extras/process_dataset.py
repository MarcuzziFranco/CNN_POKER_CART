import os
import cv2
import numpy as np

def preprocess_dataset(input_folder, output_folder, image_size=(128, 128), normalize=True):
    """
    Preprocesa un dataset escalando las imágenes a un tamaño uniforme y opcionalmente normalizándolas.

    Args:
        input_folder (str): Carpeta de entrada con subcarpetas de entrenamiento, validación y prueba.
        output_folder (str): Carpeta de salida para las imágenes preprocesadas.
        image_size (tuple): Tamaño al que se escalarán las imágenes (ancho, alto).
        normalize (bool): Si True, normaliza los valores de píxeles entre 0 y 1.

    """
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recorrer las subcarpetas (train, val, test)
    for subset in ["train", "val", "test"]:
        input_subset_folder = os.path.join(input_folder, subset)
        output_subset_folder = os.path.join(output_folder, subset)

        # Crear la carpeta de salida para el subconjunto
        if not os.path.exists(output_subset_folder):
            os.makedirs(output_subset_folder)

        # Procesar las imágenes en el subconjunto
        for image_file in os.listdir(input_subset_folder):
            input_image_path = os.path.join(input_subset_folder, image_file)

            # Leer la imagen
            image = cv2.imread(input_image_path)
            if image is None:
                print(f"Error al leer la imagen: {input_image_path}")
                continue

            # Escalar la imagen al tamaño uniforme
            resized_image = cv2.resize(image, image_size, interpolation=cv2.INTER_AREA)

            # Normalizar los valores de píxeles entre 0 y 1 si es necesario
            if normalize:
                resized_image = resized_image.astype("float32") / 255.0

            # Guardar la imagen procesada
            output_image_path = os.path.join(output_subset_folder, image_file)
            if normalize:
                # Guardar en formato .npy si está normalizado
                np.save(output_image_path.replace(".jpg", ".npy"), resized_image)
                print(f"Guardada (normalizada): {output_image_path.replace('.jpg', '.npy')}")
            else:
                # Guardar como .jpg si no está normalizado
                cv2.imwrite(output_image_path, resized_image)
                print(f"Guardada: {output_image_path}")

    print(f"Preprocesamiento completo. Dataset guardado en: {output_folder}")

#Corazon
#input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\As_corazon_dataset"  # Carpeta con las subcarpetas train, val, test
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\As_corazon_dataset_normalizado"  # Carpeta donde se guardará el dataset preprocesado
#preprocess_dataset(input_folder, output_folder, image_size=(128, 128), normalize=True)


#diamante
input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\As_diamante_dataset"  # Carpeta con las subcarpetas train, val, test
output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\As_diamante_dataset_normalizado"  # Carpeta donde se guardará el dataset preprocesado
preprocess_dataset(input_folder, output_folder, image_size=(128, 128), normalize=True)
print("finish diamante")


#picas
input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\As_picas_dataset"  # Carpeta con las subcarpetas train, val, test
output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\As_picas_dataset_normalizado"  # Carpeta donde se guardará el dataset preprocesado
preprocess_dataset(input_folder, output_folder, image_size=(128, 128), normalize=True)
print("finish picas")

#trevol
input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\As_trevol_dataset"  # Carpeta con las subcarpetas train, val, test
output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\As_trevol_dataset_normalizado"  # Carpeta donde se guardará el dataset preprocesado
preprocess_dataset(input_folder, output_folder, image_size=(128, 128), normalize=True)
print("finish trevol")