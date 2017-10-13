from tkinter import *
import pandas as pd
#from final import out
from input import input
from superimpose import superimpose
import final
from final import out
#from auto_fest import get_fest
import os
import sys
import tensorflow as tf
import numpy as np
import scipy.io
import scipy.misc

import pandas as pd


class Body():
    def __init__(self):
        super().__init__()

    def get_cover_page(self):
        
        var=out()
        #input()
        #im_path=input()[0]
        #fest=input()[1]
        """
        style_layer=["conv1_1","conv2_1","conv3_1","conv4_1","conv5_1"]
        #intializing output directory
        output_dir="./output"
        #image_for_style="./style_images/"+fest+".jpg"
        #content_image=im_path

        image_width=800
        image_height=600
        color_channels=3

        beta=5#less content ratio
        alpha=200#or else try 200
        l=1e4

        mean_values= np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))
        vgg = scipy.io.loadmat("vgg.mat")
        layers = vgg['layers']  # 0 l 0 0 2 0 0
        
      
        #var="./output/900.jpg"
        """
        temp=final.fest
        superimpose(var,temp)

b=Body()
b.get_cover_page()