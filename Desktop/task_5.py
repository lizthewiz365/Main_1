import os # imports module that uses methods for interacting with the operating
          #system
import cv2 # imports module that has functions for image processing 

def cell_movie(): # define function for creating cell movie 
        
        directory = "100K cells" # set variable for directory to folder
        files = [file for file in os.listdir(directory) if file.endswith(".png")] # compiles list of files from directory folder
        
        frame = cv2.imread(os.path.join(directory,files[0])) # reads each file in the directory folder as a frame
        height, width, layers = frame.shape # set variables for height, width and layers of shape of each frame
        
        video = cv2.VideoWriter("cellmovie.avi", 0, 10, (width, height)) # saves output video to a directory with desired fps, width and height
        
        for file in files: # loops over each file in the folder to joins them together to create a video
                video.write(cv2.imread(os.path.join(directory,file)))
        
        cv2.destroyAllWindows()
        video.release()
        

cell_movie()