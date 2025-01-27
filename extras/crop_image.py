from PIL import Image, ImageDraw
import os
import random

def random_crop(image, crop_size):
    width, height = image.size
    left = random.randint(0, width - crop_size)
    top = random.randint(0, height - crop_size)

    right = left + crop_size
    bottom = top + crop_size

    return image.crop((left, top, right, bottom))

def inverse_random_crop(image, crop_size):
    width, height = image.size

    # Asegúrate de que el tamaño del recorte no sea mayor al tamaño original
    if crop_size >= min(width, height):
        raise ValueError("El tamaño del recorte debe ser menor que las dimensiones mínimas de la imagen.")

    left = random.randint(0, width - crop_size)
    top = random.randint(0, height - crop_size)

    # Divide la imagen en cuadrantes, el recorte será uno de ellos
    if random.choice([True, False]):
        new_left, new_top = 0, 0
        new_right, new_bottom = left + crop_size, top + crop_size
    else:
        new_left, new_top = left, top

    if random.choice([True, False]):
        new_right, new_bottom = width, height
    else:
        new_right, new_bottom = left + crop_size + (width - (left + crop_size)), top + crop_size + (height - (top + crop_size))

    return image.crop((new_left, new_top, new_right, new_bottom))


def create_hole_in_image(image, hole_size):
    width, height = image.size

    # Asegúrate de que el tamaño del agujero no sea mayor al tamaño original
    if hole_size[0] >= width or hole_size[1] >= height:
        raise ValueError("El tamaño del agujero debe ser menor que las dimensiones de la imagen.")

    left = random.randint(0, width - hole_size[0])
    top = random.randint(0, height - hole_size[1])

    # Crea un objeto Draw para manipular la imagen
    draw = ImageDraw.Draw(image)

    # Dibuja el agujero con un color transparente o negro (dependiendo del modo de la imagen)
    if image.mode == 'RGBA':
        box = [(left, top), (left + hole_size[0], top + hole_size[1])]
        draw.rectangle(box, fill=(255, 255, 255, 0)) # RGBA con transparencia
    else:
        draw.rectangle([(left, top), (left + hole_size[0], top + hole_size[1])], fill=0) # Blanco o negro

    return image


def process_images_with_random_crops(input_folder, output_folder,action_crop=True,action_hole=False,inverse=False, range_crop=[50,200], num_crops=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)

            with Image.open(input_path) as img:
                for i in range(num_crops):
                    # Realiza un recorte aleatorio
                    image = None
                    with_crop = random.randint(range_crop[0], range_crop[1])
                    height_crop = random.randint(range_crop[0], range_crop[1])

                    if(action_crop):
                        if(inverse):
                            
                            image = inverse_random_crop(img,[with_crop,height_crop] );
                        else:
                            image = random_crop(img,[with_crop,height_crop])
                    if(action_hole):
                        
                        image=create_hole_in_image(img,[with_crop,height_crop])

                    # Construye la ruta de salida para cada recorte
                    output_filename = f"{os.path.splitext(filename)[0]}_crop_{i+1}.jpg"
                    output_path = os.path.join(output_folder, output_filename)

                    # Guarda el recorte
                    image.save(output_path) # type: ignore

                    print(f"Saved crop image: {output_path}")

# Define tus directorios de entrada y salida aquí
#input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\crop"


#input_folder = "C:\\Users\\Franco\\Desktop\\test\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\test\\crop"


#process_images_with_random_crops(input_folder, output_folder,False,True,False,[50,200])