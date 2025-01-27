import os
import cv2


def transforms_single(video_path,output_folder,images_per_second=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    video_capture = cv2.VideoCapture(video_path)

    if not  video_capture.isOpened():
        print(f"Error open video:{video_path}")
        return

    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    frame_interval = int(fps/images_per_second)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))


    frame_count = 0
    image_count = 0

    while True:
        ret,frame = video_capture.read()

        if not ret:
            break
    
        if frame_count % frame_interval == 0:
            image_name = f"{video_name}_frame_{image_count:04d}.jpg"
            image_path = os.path.join(output_folder,image_name)
            cv2.imwrite(image_path,frame)
            image_count +=1

            print(f"Guardando imagen: {image_name} ({image_count} imágenes generadas)")

        frame_count += 1

        if frame_count % 10 == 0:
            print(f"Procesados {frame_count}/{total_frames} frames...")

    video_capture.release()
    print(f"Image file save in:{output_folder}")

def transforms_multiply(list_paths,output_folder,images_per_second=5):
    for path in list_paths:
        transforms_single(path,output_folder,images_per_second)