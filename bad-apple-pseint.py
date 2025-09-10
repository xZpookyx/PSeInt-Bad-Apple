import cv2
import os
import sys


def main():
    while True:
        print("Create pseint file")
        output_name = input("Enter output file name: ")
        
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
        output_path: str = os.path.join(current_path, f"output/{output_name}.psc")
        video_fps: int = 15
        
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
            ms: float = 1000 / video_fps
            file.write("SubProceso play_video\n")
            
            # for each line in frame
            file.write("\tLimpiar Pantalla;\n")
            video_line: str = "Placeholder"
            file.write(f"\tEscribir \"{video_line}\";\n")
            
            file.write(f"\tEsperar {ms} Milisegundos;\n")
            
            file.write("FinSubProceso")
        
        sys.exit()

if __name__ == "__main__":
    main()