from PIL import Image, ImageEnhance
import os

def adjust_contrast_and_brightness(input_folder, output_folder, contrast_factor=2.2, brightness_factor=2.2):
   
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
                
                output_path = os.path.join(output_folder, f"brightness_constrast{filename}")

                # Ajusta el contraste
                enhancer = ImageEnhance.Contrast(img)
                image = enhancer.enhance(contrast_factor)

                # Ajusta el brillo
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(brightness_factor)

                image.save(output_path)

                print(f"Processed and saved:{output_path}")


#input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\brightness_constrast"

#adjust_contrast_and_brightness(input_folder,output_folder)   