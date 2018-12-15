# -*- coding: utf-8 -*-
"""
Program to make image pathology arrays using various functions
"""

import os, numpy as np, SimpleITK as sitk, csv, scipy.ndimage as scipy

image_list = [] #empty list to which image arrays will be appended
pathology_list = [] #empty list to which pathology result will be appended

def Test_Arrays(file_dir): #create image and pathology arrays for cropped test images
    
    file_number = os.listdir(file_dir) #list cropped MG files
    for patient in file_number:
        if patient.endswith(".tif"): #ensure correct file extension, no '.DS_Store'
            
            #Normalize image and get array
            image = sitk.ReadImage(file_dir+patient)  
            image = (image - min(image))/(max(image) - min(image))
            array = sitk.GetArrayFromImage(image) #get array
            
            #Look at pathology information in csv
            with open('/Users/Danielle/Documents/MASS-Test/mass_case_description_test_set.csv','r') as Test: #csv file containing pathology, shape, etc.
                reader = csv.reader(Test)
                for row in reader:
                    if str("Mass-Test_"+row[0]+"_"+row[2]+"_"+row[3]+"_crop.tif") == patient: #match file with row in csv 
                        if row[9]=="MALIGNANT": #augment malignant cases and add pathology 1 to list
                            rot15 = scipy.rotate(array, 15, reshape= False); image_list.append(rot15); pathology_list.append(1)
                            rot30 = scipy.rotate(array, 30, reshape= False); image_list.append(rot30); pathology_list.append(1)
                            rot45 = scipy.rotate(array, 45, reshape= False); image_list.append(rot45); pathology_list.append(1)
                            rot60 = scipy.rotate(array, 60, reshape= False); image_list.append(rot60); pathology_list.append(1)
                            rot75 = scipy.rotate(array, 75, reshape= False); image_list.append(rot75); pathology_list.append(1)
                            rot90 = scipy.rotate(array, 90, reshape= False); image_list.append(rot90); pathology_list.append(1)
                            rot105 = scipy.rotate(array, 105, reshape= False); image_list.append(rot105); pathology_list.append(1)
                            rot120 = scipy.rotate(array, 120, reshape= False); image_list.append(rot120); pathology_list.append(1)
                            rot135 = scipy.rotate(array, 135, reshape= False); image_list.append(rot135); pathology_list.append(1)
                            rot150 = scipy.rotate(array, 150, reshape= False); image_list.append(rot150); pathology_list.append(1)
                            rot180 = scipy.rotate(array, 180, reshape= False); image_list.append(rot180); pathology_list.append(1)
                            rot210 = scipy.rotate(array, 210, reshape= False); image_list.append(rot210); pathology_list.append(1)
                            rot225 = scipy.rotate(array, 225, reshape= False); image_list.append(rot225); pathology_list.append(1)
                            rot270 = scipy.rotate(array, 270, reshape= False); image_list.append(rot270); pathology_list.append(1)
                            rot315 = scipy.rotate(array, 315, reshape= False); image_list.append(rot315); pathology_list.append(1)
                            rot345 = scipy.rotate(array, 345, reshape= False); image_list.append(rot345); pathology_list.append(1)
                        if row[9]=="BENIGN" or "BENIGN_WITHOUT_CALLBACK": #augment benign cases and add pathology 0 to list
                            rot15 = scipy.rotate(array, 15, reshape= False); image_list.append(rot15); pathology_list.append(0)
                            rot30 = scipy.rotate(array, 30, reshape= False); image_list.append(rot30); pathology_list.append(0)
                            rot45 = scipy.rotate(array, 45, reshape= False); image_list.append(rot45); pathology_list.append(0)
                            rot75 = scipy.rotate(array, 75, reshape= False); image_list.append(rot75); pathology_list.append(0)
                            rot90 = scipy.rotate(array, 90, reshape= False); image_list.append(rot90); pathology_list.append(0)
                            rot135 = scipy.rotate(array, 135, reshape= False); image_list.append(rot135); pathology_list.append(0)
                            rot180 = scipy.rotate(array, 180, reshape= False); image_list.append(rot180); pathology_list.append(0)
                            rot225 = scipy.rotate(array, 225, reshape= False); image_list.append(rot225); pathology_list.append(0)
                            rot270 = scipy.rotate(array, 270, reshape= False); image_list.append(rot270); pathology_list.append(0)
                            rot315 = scipy.rotate(array, 315, reshape= False); image_list.append(rot315); pathology_list.append(0)
        
            print("done:", patient)
    
    #Lists-> np arrays
    test_image_array = np.asarray(image_list) 
    test_pathology_array = np.asarray(pathology_list) 
    return test_image_array, test_pathology_array

def Training_Arrays(file_dir): #create image and pathology arrays for cropped training images
    
    file_number = os.listdir(file_dir) #list cropped MG files
    for patient in file_number:
        if patient.endswith(".tif"): #ensure correct file extension, no '.DS_Store'
           
            #Normalize image and get array
            image = sitk.ReadImage(file_dir+patient)  
            image = (image - min(image))/(max(image) - min(image))
            array = sitk.GetArrayFromImage(image)
            
            #Look at pathology information in csv
            with open('/Users/Danielle/Documents/MASS-Training/mass_case_description_train_set.csv','r') as Training: #csv file containing pathology, shape, etc.
                reader = csv.reader(Training)
                for row in reader:
                    if str("Mass-Training_"+row[0]+"_"+row[2]+"_"+row[3]+"_crop.tif") == patient: #match file with row in csv 
                        if row[9]=="MALIGNANT": #augment malignant cases and add pathology 1 to list
                            rot15 = scipy.rotate(array, 15, reshape= False); image_list.append(rot15); pathology_list.append(1)
                            rot30 = scipy.rotate(array, 30, reshape= False); image_list.append(rot30); pathology_list.append(1)
                            rot45 = scipy.rotate(array, 45, reshape= False); image_list.append(rot45); pathology_list.append(1)
                            rot60 = scipy.rotate(array, 60, reshape= False); image_list.append(rot60); pathology_list.append(1)
                            rot75 = scipy.rotate(array, 75, reshape= False); image_list.append(rot75); pathology_list.append(1)
                            rot90 = scipy.rotate(array, 90, reshape= False); image_list.append(rot90); pathology_list.append(1)
                            rot105 = scipy.rotate(array, 105, reshape= False); image_list.append(rot105); pathology_list.append(1)
                            rot120 = scipy.rotate(array, 120, reshape= False); image_list.append(rot120); pathology_list.append(1)
                            rot135 = scipy.rotate(array, 135, reshape= False); image_list.append(rot135); pathology_list.append(1)
                            rot150 = scipy.rotate(array, 150, reshape= False); image_list.append(rot150); pathology_list.append(1)
                            rot180 = scipy.rotate(array, 180, reshape= False); image_list.append(rot180); pathology_list.append(1)
                            rot210 = scipy.rotate(array, 210, reshape= False); image_list.append(rot210); pathology_list.append(1)
                            rot225 = scipy.rotate(array, 225, reshape= False); image_list.append(rot225); pathology_list.append(1)
                            rot270 = scipy.rotate(array, 270, reshape= False); image_list.append(rot270); pathology_list.append(1)
                            rot315 = scipy.rotate(array, 315, reshape= False); image_list.append(rot315); pathology_list.append(1)
                            rot330 = scipy.rotate(array, 330, reshape= False); image_list.append(rot330); pathology_list.append(1)
                            rot345 = scipy.rotate(array, 345, reshape= False); image_list.append(rot345); pathology_list.append(1)
                        if row[9]=="BENIGN" or "BENIGN_WITHOUT_CALLBACK": #augment benign cases and add pathology 0 to list
                            rot15 = scipy.rotate(array, 15, reshape= False); image_list.append(rot15); pathology_list.append(0)
                            rot30 = scipy.rotate(array, 30, reshape= False); image_list.append(rot30); pathology_list.append(0)
                            rot45 = scipy.rotate(array, 45, reshape= False); image_list.append(rot45); pathology_list.append(0)
                            rot60 = scipy.rotate(array, 60, reshape= False); image_list.append(rot60); pathology_list.append(0)
                            rot75 = scipy.rotate(array, 75, reshape= False); image_list.append(rot75); pathology_list.append(0)
                            rot90 = scipy.rotate(array, 90, reshape= False); image_list.append(rot90); pathology_list.append(0)
                            rot105 = scipy.rotate(array, 105, reshape= False); image_list.append(rot105); pathology_list.append(0)
                            rot120 = scipy.rotate(array, 120, reshape= False); image_list.append(rot120); pathology_list.append(0)
                            rot135 = scipy.rotate(array, 135, reshape= False); image_list.append(rot135); pathology_list.append(0)
                            rot150 = scipy.rotate(array, 150, reshape= False); image_list.append(rot150); pathology_list.append(0)
                            rot180 = scipy.rotate(array, 180, reshape= False); image_list.append(rot180); pathology_list.append(0)
                            rot210 = scipy.rotate(array, 210, reshape= False); image_list.append(rot210); pathology_list.append(0)
                            rot225 = scipy.rotate(array, 225, reshape= False); image_list.append(rot225); pathology_list.append(0)
                            rot270 = scipy.rotate(array, 270, reshape= False); image_list.append(rot270); pathology_list.append(0)
                            rot315 = scipy.rotate(array, 315, reshape= False); image_list.append(rot315); pathology_list.append(0)
                            rot330 = scipy.rotate(array, 330, reshape= False); image_list.append(rot330); pathology_list.append(0)
            
            print("done:", patient)
    
    #Lists-> np arrays
    training_image_array = np.asarray(image_list) 
    training_pathology_array = np.asarray(pathology_list) 
    return training_image_array, training_pathology_array

def Concatenate(training_image_array, training_pathology_array, test_image_array, test_pathology_array):
    
    #Concatenate training and test image and pathology arrays
    final_image_array = np.concatenate((training_image_array, test_image_array),axis=0)
    final_pathology_array = np.concatenate((training_pathology_array, test_pathology_array),axis=0)
    optimized_final_image_array = (final_image_array - np.mean(final_image_array, axis = 0))/np.std(final_image_array, axis = 0) #Optimize array (zero mean, unit variance)
    
    #Save arrays
    np.save("/Users/Danielle/Documents/Arrays/image_array", optimized_final_image_array) #save image array
    np.save("/Users/Danielle/Documents/Arrays/pathology_array", final_pathology_array) #save pathology label array

def main():
    test_image_array, test_pathology_array = Test_Arrays("/Users/Danielle/Documents/MASS-Test/cropped/")
    training_image_array, training_pathology_array = Training_Arrays("/Users/Danielle/Documents/MASS-Training/cropped/")
    Concatenate(training_image_array, training_pathology_array, test_image_array, test_pathology_array)
    
main()
