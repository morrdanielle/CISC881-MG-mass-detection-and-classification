#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:41:19 2018

@author: Danielle
"""

import os, SimpleITK as sitk

def Move_Files(): #get rid off unncessary layers of folders, moving MG images to main folder and renaming images based on patient name and breast view
    
    #find images by accessing all the folders they are contained within
    file_dir = "/Users/Danielle/Documents/MASS-Test-dcm/"
    file_dir1 = os.listdir(file_dir)
    
    for folder in file_dir1:
        if folder.startswith('.DS_Store'): #to get rid of .DS_Store file
            folder = None
            continue
        folder_dir = os.path.join(file_dir, folder)  #join folders
        folder_dir1 = os.listdir(folder_dir) #list files in new folder
        #print(folder_dir1) #see what folders are contained within the new folder, can do this at each step
        
        """ * * * Repeat previous step until images are located! * * * """
    
        for mammogram in folder_dir1:
            if mammogram.startswith('.DS_Store'): 
                mammogram = None
                continue
            mammogram_dir = os.path.join(folder_dir, mammogram) #THIS IS WHERE THE PATIENT NUMBER AND BREAST VIEW ARE PRESENTED
            mammogram_dir1 = os.listdir(mammogram_dir)
    
            for image in mammogram_dir1:
                if image.startswith('.DS_Store'):
                    image = None
                    continue
                image_dir = os.path.join(mammogram_dir, image)
                image_dir1 = os.listdir(image_dir)
    
                for x in image_dir1:
                    if x.startswith('.DS_Store'):
                        x = None
                        continue
                    DIR = os.path.join(image_dir, x) #THIS FOLDER CONTAINS THE IMAGES
    
                    for filename in os.listdir(DIR): #loop through files in image folder
                        if filename.startswith('000000.dcm'): #Original MG image names
                            os.rename(os.path.join(DIR,filename), os.path.join(file_dir, str(mammogram_dir)+".dcm")) #move to main directory and rename based on patient name and breast view
                            print("done :", filename)

def tiff_Convert(): #convert the renamed dcm images to tiff images
    
    file_dir = '/Users/Danielle/Documents/MASS-Test-dcm/' #where files are stored
    output_dir = '/Users/Danielle/Documents/MASS-Test-tif/' #where new files are added
    all_patient_number = os.listdir(file_dir)
    for patient in all_patient_number:
        if patient.endswith('.dcm'): #to get rid of .DS_Store file
            reader = sitk.ImageFileReader()
            reader.SetFileName(file_dir+patient)
            image = reader.Execute(); #read image
            writer = sitk.ImageFileWriter()
            writer.SetFileName(output_dir+str(patient)[:-4]+".tif")
            writer.Execute(image) #write image, converting to tiff
            print("done :", patient)
            
def main():
    Move_Files()
    tiff_Convert()
    
main()