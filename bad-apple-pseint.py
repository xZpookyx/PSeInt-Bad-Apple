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
        
        current_path: str = sys.path[0]
        output_path: str = os.path.join(current_path, f"output/{output_name}.psc")
            
        with open(output_path, "w") as file:
            
            
            file.write("Hi")
            file.write("Hi2")
        
        sys.exit()

if __name__ == "__main__":
    main()