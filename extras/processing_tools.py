import os
import video_to_image
import rotation_image as rot
import flip_image as flip
import crop_image as crop
import brightness_constrast_image as bc
import gaussiano_image as noise


paths_as_corazon = [
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_amarillo.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_cuadriculado.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_madera.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_mantel.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_negro.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_pasto.mp4",
]

#video_path = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_corazon_amarillo.mp4"
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\base"

paths_as_diamante = [
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_diamante_amarillo.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_diamante_cuadriculado.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_diamante_madera.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_diamante_mantel.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_diamante_negro.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_diamante_pasto.mp4",
]


paths_as_trevol = [
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_trevol_amarillo.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_trevol_cuadriculado.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_trevol_madera.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_trevol_mantel.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_trevol_negro.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_trevol_pasto.mp4",
]


paths_as_picas = [
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_picas_amarillo.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_picas_cuadriculado.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_picas_madera.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_picas_mantel.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_picas_negro.mp4",
    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\original_videos\\as_picas_pasto.mp4",
]

output_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\base"
output_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\base"
output_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\base"


#video_to_image.transforms_single("path_unico",output_folder)

#video_to_image.transforms_multiply(paths_as_diamante,output_folder)
#video_to_image.transforms_multiply(paths_as_trevol,output_folder_trevol)
#video_to_image.transforms_multiply(paths_as_picas,output_folder_picas)

"""FINISH PROCESS VIDEO"""

"""Rotate"""
"""
input_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\base"
input_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\base"
input_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\base"

output_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\rotate"
output_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\rotate"
output_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\rotate"

rot.rotate_images_lote(input_folder_diamante , output_folder_diamante, angles=[-10, 10, 15, -15])
rot.rotate_images_lote(input_folder_trevol , output_folder_trevol, angles=[-10, 10, 15, -15])
rot.rotate_images_lote(input_folder_picas , output_folder_picas, angles=[-10, 10, 15, -15])
"""
"""Rotate finish"""

"""Flip"""
"""
input_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\base"
input_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\base"
input_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\base"

output_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\flip"
output_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\flip"
output_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\flip"

flip.flip_images(input_folder_diamante,output_folder_diamante)
flip.flip_images(input_folder_trevol,output_folder_trevol)
flip.flip_images(input_folder_picas,output_folder_picas)
"""
"""Flip finish"""


"""Brightness"""
"""
input_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\base"
input_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\base"
input_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\base"

output_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\brightness_constrast"
output_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\brightness_constrast"
output_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\brightness_constrast"

bc.adjust_contrast_and_brightness(input_folder_diamante,output_folder_diamante)
bc.adjust_contrast_and_brightness(input_folder_trevol,output_folder_trevol)
bc.adjust_contrast_and_brightness(input_folder_picas,output_folder_picas)
"""
"""Brightness Finish"""


"""Crop"""
"""
input_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\base"
input_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\base"
input_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\base"

output_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\crop"
output_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\crop"
output_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\crop"

crop.process_images_with_random_crops(input_folder_diamante, output_folder_diamante,False,True,False,[50,200])
crop.process_images_with_random_crops(input_folder_trevol, output_folder_trevol,False,True,False,[50,200])
crop.process_images_with_random_crops(input_folder_picas, output_folder_picas,False,True,False,[50,200])
"""
"""Crop Finish """

"""Gaussiano"""

input_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\base"
input_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\base"
input_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\base"

output_folder_diamante = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_diamante\\gaussiano"
output_folder_trevol =   "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_trevol\\gaussiano"
output_folder_picas =    "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_picas\\gaussiano"

noise.process_images_with_noise(input_folder_diamante, output_folder_diamante)
noise.process_images_with_noise(input_folder_trevol, output_folder_trevol)
noise.process_images_with_noise(input_folder_picas, output_folder_picas)

"""Gaussiano Finish"""

#process_images_with_random_crops(input_folder, output_folder,False,True,False,[50,200])