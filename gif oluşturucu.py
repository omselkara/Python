import imageio
import os,cv2
from PIL import Image
import numpy as np
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def gif(path):
    image_folder = os.fsencode(path)

    filenames = []

    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.jpeg', '.png', '.gif') ):
            filenames.append(path+filename)

    filenames.sort() # this iteration technique has no built in order, so sort the frames

    images = list(map(lambda filename: imageio.imread(filename), filenames))

    imageio.mimsave(os.path.join('movie.gif'), images, duration = 0.04) # modify duration as needed

            
        
                    
