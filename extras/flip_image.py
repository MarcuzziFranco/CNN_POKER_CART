import os
from PIL import Image
from numpy import imag

def flip_images(input_folder, output_folder):
    # Asegúrate de que la carpeta de salida exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Itera sobre cada archivo en el directorio de entrada
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Construye la ruta completa del archivo
            input_path = os.path.join(input_folder, filename)

            # Abre la imagen
            with Image.open(input_path) as img:
                # Voltea la imagen horizontalmente (al revés horizontal)
                flipped_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT) # type: ignore

                # Voltea la imagen verticalmente (al revés vertical)
                flipped_vertical = img.transpose(Image.FLIP_TOP_BOTTOM) # type: ignore

                # Construye las rutas completas de salida
                output_path_horizontal = os.path.join(output_folder, f"horizontal_{filename}")
                output_path_vertical = os.path.join(output_folder, f"vertical_{filename}")

                # Guarda las imágenes volteadas en la carpeta de salida
                flipped_horizontal.save(output_path_horizontal)
                flipped_vertical.save(output_path_vertical)

                print(f"Processed and saved: {output_path_horizontal}, {output_path_vertical}")


#input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\flip"

#flip_images(input_folder,output_folder)