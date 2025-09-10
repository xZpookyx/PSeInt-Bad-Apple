import cv2
import numpy as np
from numpy.typing import NDArray
import os
import sys

def light_to_ascii(light: int) -> str:
    ascii_chars =  " .:-=+*#%@"

    if light > 255: light = 255
    if light < 0: light = 0
    light = round(light / 255 * len(ascii_chars))
    
    return ascii_chars[light]
    

def main():
    while True:
        print("Create pseint file")
        # output_name = input("Enter output file name: ")
        
        # video_path = input("Enter source video path: ")
        
        # if not os.path.exists(video_path):
        #     print("Video does not exist")
        #     continue
        
        # if not video_path.endswith(".mp4"):
        #     print("Video is not a valid video file")
        #     continue
        
        # TODO: Eng / Esp languages
        language: int = 0
        
        current_path: str = sys.path[0]
        video_path: str = os.path.join(current_path, "Bad apple.mp4")
        output_path: str = os.path.join(current_path, f"output/bad_apple.psc")
        video_fps: int = 15
        resolution: tuple[int, int] = (70, int(70 / (4/3)))
        
        # Generate file
        with open(output_path, "w") as file:
            # Entry
            entry_text: str
            if language == 0:
                entry_text = "Press a key to play Bad Apple"
            else:
                entry_text = "Presiona una tecla para reproducir Bad Apple"
            
            file.write(
                "Algoritmo bad_apple\n"
                f"\tEscribir \"{entry_text}\";\n"
                "\tEsperar Tecla;\n"
                "\tplay_video;\n"
                "FinAlgoritmo\n"
                "\n"
                )
            
            # Video frames
            cap: cv2.VideoCapture = cv2.VideoCapture(video_path)
            ms: float = 1000 / video_fps
            
            if not cap.isOpened():
                file.write(
                    "SubProceso play_video\n"
                    "\tEscribir \"Error\";\n"
                    "FinSubProceso"
                )
                cap.release()
                break
            
            
            file.write("SubProceso play_video\n")
            
            # for each line in frame
            cap.set(cv2.CAP_PROP_FPS, video_fps)
            
            for frame_index in range(1):
                file.write("\tLimpiar Pantalla;\n")
                
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame = cv2.resize(frame, (resolution))
                gray: NDArray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                for i in range(gray.shape[0]):
                    row: str = ""
                    for j in range(gray.shape[1]):
                        row += light_to_ascii(gray[0][1])
                    file.write(f"\tEscribir \"{row}\";\n")
                
                file.write(f"\tEsperar {ms} Milisegundos;\n")
            
            file.write("FinSubProceso")
        
        sys.exit()

if __name__ == "__main__":
    main()