#PythonResumirDAV.py

#Autor. Héctor Jorquera C.
#Fecha. 06-01-2023
#Objet. Extraer el primer y ultimo frame desde un archivo DAT a un archivo AVI

#Modif. Héctor Jorquera C.
#Fecha. 06-01-2023
#Objet. Extraer los primeros tres segundos desde un archivo DAT a un archivo AVI

import os
import cv2

# Función para crear el resumen del video: Extraer Primer y Ultimo Frame de cada Video
def create_video_summary(video_path, output_path):
    print(video_path +' - ' + output_path + '\n')


    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        exit(1)

    # Get the frame width and height
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Read the first frame
    ret, first_frame = cap.read()

    # Read the last frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
    ret, last_frame = cap.read()

    # Create a VideoWriter object
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 50, (frame_width, frame_height))

    # Write the first frame to the output file
    out.write(first_frame)

    # Write the last frame to the output file
    out.write(last_frame)

    # Close the output file
    out.release()

    # Close the video file
    cap.release()

    # Destroy the window
    cv2.destroyAllWindows()

# Función para crear el resumen del video: Extraer 3 segundos de cada Video
def create_video_summary_3Seconds(video_path, output_path):
    print(video_path + ' - ' + output_path + '\n')

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        exit(1)

    # Get the frame width and height
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Calculate the number of frames to extract for 3 seconds
    fps = cap.get(cv2.CAP_PROP_FPS)
    num_frames = int(fps * 3)

    # Create a VideoWriter object
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (frame_width, frame_height))

    # Read and write the frames for 3 seconds
    for _ in range(num_frames):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    # Close the output file
    out.release()

    # Close the video file
    cap.release()

    # Destroy the window
    cv2.destroyAllWindows()
# Función para procesar los archivos de video en un directorio y sus subdirectorios
def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.dav'):
                print(file + '\n')
                video_path = os.path.join(root, file)
                #output_path = os.path.join(root, 'summary_' + file + '.avi')
                output_path = os.path.join('K:\\NVR_SUMMARY\\T2_Norte\\' + file + '.avi')
                #create_video_summary(video_path, output_path)
                create_video_summary_3Seconds(video_path, output_path)

# Se especifica el directorio base donde se buscarán los archivos de video
if __name__ == "__main__":
    base_dir = "K:\\NVR_SUMMARY\\T2_Norte\\"   #"C:\\Users\\hjorquera\\Desktop\\DAV"
    base_dir = base_dir.encode('latin1').decode('utf-8')
    process_directory(base_dir)