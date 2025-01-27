from PIL import Image, ImageDraw, ImageFilter
import os
import numpy as np
import cv2

def add_gaussian_noise(image, mean=0, std_dev=25):
    # Convierte la imagen en un array de NumPy
    image_array = np.array(image)

    # Genera ruido gaussiano
    noise = np.random.normal(mean, std_dev, image_array.shape).astype(np.uint8)

    # Añade el ruido a la imagen original
    noisy_image_array = cv2.add(image_array, noise)

    # Convierte de nuevo el array al objeto Image
    noisy_image = Image.fromarray(noisy_image_array)

    return noisy_image

def process_images_with_noise(input_folder, output_folder, mean=0, std_dev=25):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)

            with Image.open(input_path) as img:
                # Añade ruido a la imagen
                noisy_image = add_gaussian_noise(img, mean, std_dev)

                # Construye la ruta de salida para la imagen con ruido
                output_filename = f"{os.path.splitext(filename)[0]}_noisy.png"
                output_path = os.path.join(output_folder, output_filename)

                # Guarda la imagen con el ruido añadido
                noisy_image.save(output_path)

                print(f"Saved: {output_path}")

# Define tus directorios de entrada y salida aquí
#input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\gaussiano"

#input_folder = "C:\\Users\\Franco\\Desktop\\test\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\test\\gaussiano"

#process_images_with_noise(input_folder, output_folder)