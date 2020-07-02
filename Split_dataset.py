# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:10:39 2020

@author: Yasmi
"""
import os
path="dataset\hump\hump\data"
import numpy as np
import shutil
files=os.listdir(path)
file_wo_extension=[]

path_read_Annot="dataset\hump\hump\dataAnot"

path_write_trainL="dataset\\hump\\hump\\data_train\\label"
path_write_trainF="dataset\\hump\\hump\\data_train\\feature"
path_write_valL="dataset\\hump\\hump\\data_val\\label"
path_write_valF="dataset\\hump\\hump\\data_val\\feature"
for i in files:
    file_wo_extension.append(i[:-4])
#print(file_wo_extension)
np.random.seed(0)
np.random.shuffle(file_wo_extension)
print(file_wo_extension)

splitData = int(0.8*len(file_wo_extension))
valid_ints = file_wo_extension[splitData:]
train_ints = file_wo_extension[:splitData]

for v in valid_ints:    
    print(os.path.join(path,v)+".jpg")
    print(os.path.join(path_read_Annot,v)+".xml")
    print(os.path.join(path_write_valL,v)+".xml")
    print(os.path.join(path_write_valF,v)+".jpg")
    shutil.copy(os.path.join(path,v)+".jpg",os.path.join(path_write_valF,v)+".jpg")
    shutil.copy(os.path.join(path_read_Annot,v)+".xml",os.path.join(path_write_valL,v)+".xml")
  
    
for t in train_ints:
    print(os.path.join(path,t)+".jpg")
    print(os.path.join(path_read_Annot,t)+".xml")
    print(os.path.join(path_write_trainL,t)+".xml")
    print(os.path.join(path_write_trainF,t)+".jpg")
    shutil.copy(os.path.join(path,t)+".jpg",os.path.join(path_write_trainF,t)+".jpg")
    shutil.copy(os.path.join(path_read_Annot,t)+".xml",os.path.join(path_write_trainL,t)+".xml")
    
