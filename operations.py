"""
The module comprises of the different operations to be performed on images
"""

import cv2
import os
import numpy as np
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from basicsr.utils.download_util import load_file_from_url

modelUrl = 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth'
uploadsPic = '/home/ekkelai/Documents/Tasks/GFPGAN Task/Temppics'
modelDir = 'ModelDirectory'


def upsampling_image(filePath: str, scale: int)-> str:
    """
    The function upsamples an image

    Parameters
    ----------
    str
    int

    Returns
    -------
    str

    """


    newImage = cv2.imread(filePath)
    modelPath = load_file_from_url(modelUrl, os.path.join(modelDir, 'weights'), progress = True, file_name = None)
    print(modelPath)
    model = RRDBNet(num_in_ch = 3, num_out_ch = 3, num_feat = 64, num_block = 23, num_grow_ch = 32, scale = scale)
    print(model)
    upSampler = RealESRGANer(scale, modelPath, model)
    outputImage = upSampler.enhance(newImage, scale)
    fileName = 'newimg.jpg'
    cv2.imwrite('newimg.jpg', outputImage)
    cv2.imshow(outputImage)
    path = os.path.join(uploadsPic, fileName)
    print(path)
    return path
