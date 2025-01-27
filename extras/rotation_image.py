import cv2 
import os 
import numpy as np

def rotate_image(image,angle):
    """
    Rotate image by angle

    Args:
        image: image to rotate type (array NumPy)
        angle: value of the angle to rotate

    Returns:
        Rotated image
    """
    (h,w) = image.shape[:2] # Height and Witght to image.
    center = (w// 2, h// 2) # Center to image.

    rotation_matrix = cv2.getRotationMatrix2D(center,angle,1.0)
    rotated = cv2.warpAffine(image,rotation_matrix,(w,h))

    return rotated

def rotate_images_lote(input_folder,output_folder,angles = [-10,10]):
    """
    Apply rotations to all images in the folder

    Args
        input_folder: Folder input images.
        output_folder: Folder output save images rotated
        angles: Range of angles to rotate the images
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder,filename)

        #Read image
        image = cv2.imread(input_path)
        if image is None:
            print(f"Error to load image: {input_path}")
            continue
        
        print("Begin image rotate {input_path}")

        for angle in angles:
            #Rotate image
            img_rot = rotate_image(image,angle)

            base_name,ext = os.path.splitext(filename)
            output_name = f"{base_name}_rotated_{angle}{ext}"
            output_path = os.path.join(output_folder,output_name)
            
            cv2.imwrite(output_path,img_rot)
            print(f"Save image:{output_path}")


#input_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\base"
#output_folder = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\frame_raw\\as_corazon\\rotate"

#rotate_images_lote(input_folder , output_folder, angles=[-10, 10, 15, -15])