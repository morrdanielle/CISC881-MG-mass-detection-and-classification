# CISC881-MG-mass-detection-and-classification

This repository contains code that was used for computer-aided detection and diagnosis of mass lesions in mammograms from the CBIS-DDSM collection in The Cancer Imaging Archive. The file description and order of execution are listed below:

1-Maneuver_Files.py: Take all the MG images downloaded directly from TCIA, renames them based on patient name/breast view (ex: Mass-Test_P_00369_LEFT_CC.dcm) and moved them to a common folder. It also converts the dcm extension to tif. This makes looping through files much easier and simplifies the next few files of code.

2-Segment_Crop.m: This program loops through the MG .tiff files, performing preprocessing steps to remove noise, segmentation to detect the mass ROI, and cropping of the image around this ROI.

3-Create_Arrays.py: Includes functions to create arrays for the cropped test images and for the cropped training images, which are then concatentate (training+test) and the 3D image array is optimized for zero mean and unit variance. The optimized image array and pathology array are then saved.

4-CNN_model.ipynb: A convolutional neural network used to predict pathology of the tumours as either 1 (malignant) or 0 (benign) 
