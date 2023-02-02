"""
The module comprises of the driver program to run the application
"""

from operations import upsampling_image

directoryPath = '/home/ekkelai/Dcouments/Tasks/GFPGAN Task/noisyimage.jpg'

if __name__ == '__main__':
    upsampling_image(directoryPath, 4)
