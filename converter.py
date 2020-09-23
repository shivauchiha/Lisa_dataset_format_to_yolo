import pandas as pd
import numpy as np
import os
import glob
import cv2

curr_path = os.getcwd()


Annotation_path = curr_path+"/Data/Annotations/Annotations"
image_path = curr_path+"/Data"
Yolo = curr_path+"/Yolo"


an_files = glob.glob(Annotation_path+'/*')
img_files = glob.glob(image_path+'/*')
img_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/Annotations')
img_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/sample-nightClip1')
img_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/sample-dayClip6')
img_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/dayTrain')
img_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/nightTrain')
an_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/Annotations/Annotations/dayTrain')
an_files.remove('/home/shyam/Downloads/LISA_Annotation/Data/Annotations/Annotations/nightTrain')


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def generate(anncsv,curr_path,an_files,Yolo):
    class_list ={"stop":0,"go":1,"stopLeft":2,"goForward":3,"goLeft":4,"warning":5,"warningLeft":6}
    print ("progressing")
    for index, row in anncsv.iterrows():
        img_name=os.path.basename(os.path.splitext(an_csv.iloc[index]['Filename'])[0])
        ux=an_csv.iloc[index]['Upper left corner X']
        uy=an_csv.iloc[index]['Upper left corner Y']
        lx=an_csv.iloc[index]['Lower right corner X']
        ly=an_csv.iloc[index]['Lower right corner Y']
        box = [ux,lx,uy,ly]
        img_path_data_sel = os.path.basename(os.path.splitext(an_files)[0])
        img_path = curr_path+"/Data"+"/"+img_path_data_sel+"/"+img_path_data_sel+"/frames"
        img_file_name = os.path.basename(anncsv.iloc[index]['Filename'])
        image = cv2.imread(img_path +"/"+img_file_name)
        x,y,width,height = convert([image.shape[1],image.shape[0]],box)
        class_id = class_list[an_csv.iloc[index]['Annotation tag']]
        cv2.imwrite(Yolo+"/"+img_name+".jpg", image)
        file1 = open(Yolo+"/"+img_name+".txt","a")
        file1.write("{} {} {} {} {}\n".format(class_id,x,y,width,height))
        file1.close()
        
    print ("complete {}".format(img_path_data_sel))   




for i in an_files:
    an_csv=pd.read_csv(i+'/frameAnnotationsBOX.csv',sep=';')
    generate(an_csv,curr_path,i,Yolo)



















