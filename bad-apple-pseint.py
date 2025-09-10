import cv2
import math
import numpy as np
import os
import sys

def light_to_ascii(light: int) -> str:
    ascii_chars =  " .:-=+*#%@"
    
    if light > 255: light = 255
    if light < 0: light = 0
    light = round(light / 255 * (len(ascii_chars) - 1))
    
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
        video_fps: int = 1
        resolution: tuple[int, int] = (70, int(70 / 3.5))
        
        # Generate file
        with open(output_path, "w") as file:
            # Entry
            title_text: str 
            entry_text: str
            if language == 0:
                title_text = "!! Rescale the screen until the box fits !!"
                entry_text = "Press a key to play Bad Apple"
            else:
                title_text = "!! Reescala la pantalla hasta que se encuadre la caja !!"
                entry_text = "Presiona una tecla para reproducir Bad Apple"
            
            # Start algorithm
            file.write("Algoritmo bad_apple\n")
            
            # Head
            file.write("\tLimpiar pantalla;\n")
            file.write("\t Escribir ")
            file.write("\"" + "@" * resolution[0] + "\";\n")
            file.write("\t Escribir ")
            file.write("\"@" + " " * (resolution[0] - 2) + "@\";\n")
            
            # Title
            file.write("\t Escribir ")
            file.write("\"@" + " " * math.floor((resolution[0] - 2 - len(title_text)) / 2) )
            file.write(title_text)
            file.write(" " * math.ceil((resolution[0] - 2 - len(title_text)) / 2) + "@\";\n")
            
            # Separation
            file.write("\t Escribir ")
            file.write("\"@" + " " * (resolution[0] - 2) + "@\";\n")
            
            # Entry
            file.write("\t Escribir ")
            file.write("\"@" + " " * math.floor((resolution[0] - 2 - len(entry_text)) / 2) )
            file.write(entry_text)
            file.write(" " * math.ceil((resolution[0] - 2 - len(entry_text)) / 2) + "@\";\n")
            
            # Fill
            for i in range(resolution[1] - 8):
                file.write("\t Escribir ")
                file.write("\"@" + " " * (resolution[0] - 2) + "@\";\n")
            
            # Title
            file.write("\t Escribir ")
            file.write("\"@" + " " * math.floor((resolution[0] - 2 - len(title_text)) / 2) )
            file.write(title_text)
            file.write(" " * math.ceil((resolution[0] - 2 - len(title_text)) / 2) + "@\";\n")
            
            # Separation
            file.write("\t Escribir ")
            file.write("\"@" + " " * (resolution[0] - 2) + "@\";\n")
                
            # End
            file.write("\t Escribir ")
            file.write("\"" + "@" * resolution[0] + "\";\n")
            
            
            # End algorithm
            file.write(
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
            position_ms: float = 0
            while True:
                file.write("\tLimpiar Pantalla;\n")
                cap.set(cv2.CAP_PROP_POS_MSEC, position_ms)
                
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame = cv2.resize(frame, (resolution))
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                for i in range(gray.shape[0]):
                    row: str = ""
                    for j in range(gray.shape[1]):
                        row += light_to_ascii(gray[i][j])
                    file.write(f"\tEscribir \"{row}\";\n")
                
                position_ms += ms
                file.write(f"\tEsperar {ms} Milisegundos;\n")
            
            file.write("FinSubProceso")
        
        sys.exit()

if __name__ == "__main__":
    main()