"""
The module comprises of the different operations to be performed on images
"""

import cv2
import os
import numpy as np
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from basicsr.utils.download_util import load_file_from_url

fileUrl = ['https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth']
picUploads = 'Temppics'
modelDir = 'ModelDirectory'


def upsampling_image(filePath: str)-> str:
    """
    The function upsamples an image

    Parameters
    ----------
    str

    Returns
    -------
    str

    """

    newImage = cv2.imread(filePath)
    model = RRDBNet(num_in_ch = 3, num_out_ch = 3, num_feat = 64, num_block = 23, num_grow_ch = 32, scale = 4)
    modelPath = load_file_from_url(url = fileUrl[0], model_dir = modelDir, progress = True, file_name = None)
    #print(modelPath)
    #print(model)
    upSampler = RealESRGANer(scale = 4, model_path = modelPath, dni_weight = 1, model = model)
    outputImage = upSampler.enhance(newImage, 4)
    fileName = 'upsampledimg.jpg'
    cv2.imwrite('upsampledimg.jpg', outputImage[0])
    path = os.path.join("", fileName)
    return path
