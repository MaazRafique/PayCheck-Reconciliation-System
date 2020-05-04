#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:08:43 2019

@author: maazrafique
"""

import os
import cv2
import matplotlib.pyplot as plt

folderpath='/Users/maazrafique/Documents/FYP Work/Data Set/Ideal/scanning 2271*3079'
filenames = os.listdir(folderpath)
for filename in filenames:
  #imagefile = Image.open(folderpath+'/'+filename)
   
#Path = "~/Documents/FYP Work/Data Set/Ideal/scanning 2270x3070/02.jpg"
    img = cv2.imread(folderpath+'/'+filename)
#print(img.shape)
#plt.imshow(img )
    if(filename != '.DS_Store'):
    
        img1 = img [160 : 400 , 125 : 773]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/1/'+filename[0:len(filename)-4]+'_1.jpg' , img1)
        
        img2 = img [152 : 395 , 785: 1450]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/2/'+filename[0:len(filename)-4]+'_2.jpg' , img2)
        
        img3 = img [172 : 400 , 1492 : 2090]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/3/'+filename[0:len(filename)-4]+'_3.jpg' , img3)
        
        img4 = img [380 : 590 , 120 : 765]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/4/'+filename[0:len(filename)-4]+'_4.jpg' , img4)
        
        img5 = img [376 : 595 , 805 : 1410]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/5/'+filename[0:len(filename)-4]+'_5.jpg' , img5)
        
        img6 = img [396 : 542 , 1474 : 2070]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/6/'+filename[0:len(filename)-4]+'_6.jpg' , img6)
        
        img7 = img [568 : 760 , 149 : 748]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/7/'+filename[0:len(filename)-4]+'_7.jpg' , img7)
        
        img8 = img [568 : 828 , 805 : 1410]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/8/'+filename[0:len(filename)-4]+'_8.jpg' , img8)
        
        img9 = img  [568 : 760 , 1474 : 2070]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/9/'+filename[0:len(filename)-4]+'_9.jpg' , img9)
        
        img10 = img [784 : 970 , 149 : 748]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/10/'+filename[0:len(filename)-4]+'_10.jpg' , img10)
        
        img11 = img [784 : 980 , 805 : 1410]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/11/'+filename[0:len(filename)-4]+'_11.jpg' , img11)
        
        img12 = img [784 : 980 , 1474 : 2070]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/12/'+filename[0:len(filename)-4]+'_12.jpg' , img12)
        
        img13 = img [1000 : 1220 , 149 : 748]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/13/'+filename[0:len(filename)-4]+'_13.jpg' , img13)
        
        img14 = img [1000 : 1220 , 805 : 1410]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/14/'+filename[0:len(filename)-4]+'_14.jpg' , img14)
        
        img15 = img [1000 : 1240 , 1474 : 2070]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/15/'+filename[0:len(filename)-4]+'_15.jpg' , img15)
        
        img16 = img [1220 : 1480 , 149 : 748]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/16/'+filename[0:len(filename)-4]+'_16.jpg' , img16)
        
        img17 = img [1220 : 1480 , 790 : 1410]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/17/'+filename[0:len(filename)-4]+'_17.jpg' , img17)
        
        img18 = img [1220 : 1500 , 1455 : 2070]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/18/'+filename[0:len(filename)-4]+'_18.jpg' , img18)
        
        img19 = img [1440 : 1700 , 115 : 800]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/19/'+filename[0:len(filename)-4]+'_19.jpg' , img19)
        
        img20 = img  [1440 : 1760 , 780 : 1460]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/20/'+filename[0:len(filename)-4]+'_20.jpg' , img20)
        
        img30 = img [1440 : 1760 , 1450 : 2120]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/30/'+filename[0:len(filename)-4]+'_30.jpg' , img30)
        
        img40 = img [1680 : 2010 , 115 : 800]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/40/'+filename[0:len(filename)-4]+'_40.jpg' , img40)
        
        img50 = img [1680 : 2010 , 780 : 1460]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/50/'+filename[0:len(filename)-4]+'_50.jpg' , img50)
        
        img60 = img [1680 : 2010 , 1450 : 2120]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/60/'+filename[0:len(filename)-4]+'_60.jpg' , img60)
        
        img70 = img [1920 : 2260 , 115 : 800]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/70/'+filename[0:len(filename)-4]+'_70.jpg' , img70)
        
        img80 = img [1920 : 2260 , 780 : 1470]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/80/'+filename[0:len(filename)-4]+'_80.jpg' , img80)
        
        img90 = img  [1920 : 2260 , 1450 : 2120]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/90/'+filename[0:len(filename)-4]+'_90.jpg' , img90)
        
        img100 = img [2190 : 2430 , 115 : 800]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/100/'+filename[0:len(filename)-4]+'_100.jpg' , img100)
        
        img1000 = img [2190 : 2430 , 780 : 1470]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/1000/'+filename[0:len(filename)-4]+'_1000.jpg' , img1000)
        
        IMG_lac = img [2190 : 2450 , 1450 : 2120]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/Lac/'+filename[0:len(filename)-4]+'_Lac.jpg' , IMG_lac)
        
        IMG_Crore = img [2390 : 2670 , 115 : 800]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/Crore/'+filename[0:len(filename)-4]+'_Crore.jpg' , IMG_Crore)
        
        IMG_Million = img [2400 : 2690 , 780 : 1470]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/Million/'+filename[0:len(filename)-4]+'_Million.jpg' , IMG_Million)
        
        IMG_Billion = img [2400 : 2700 , 1450 : 2120]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/Billion/'+filename[0:len(filename)-4]+'_Billion.jpg' , IMG_Billion)
        
        IMG_Trillion = img [2620 : 2940 , 115 : 800]
        cv2.imwrite('/Users/maazrafique/Documents/FYP Work/Cropped DataSet/Trillion/'+filename[0:len(filename)-4]+'_Trillion.jpg' , IMG_Trillion)
        
    



#plt.imshow(img1)