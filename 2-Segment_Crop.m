clc;    
clear all;
close all;  

% Folder containing MG files
folder = '/Users/Danielle/Documents/MASS-Training/RIGHT/';
if ~isdir(folder)
  errorMessage = sprintf('Error: The following folder does not exist:\n%s', folder);
  uiwait(warndlg(errorMessage));
  return;
end
files = fullfile(folder, '*.tif');
f = dir(files);

% Loop through files
for k = 1 : numel(f)
    Basefilename = f(k).name;
    filename = fullfile(folder, Basefilename);
    [filepath,name,ext] = fileparts(filename);

    %Read image
    Image = imread(filename);
    Image=rgb2gray(Image); %convert to gray 
    [r, c] = size(Image);
    I = imresize(Image, 2500/max(r))
    I=Image(100:r-100,350:c-50); %crop out border area containing noise, reverse "c" crop values (i.e. 50:c-350) depending on left or right view
    
    %Pre-processing
    I2 = medfilt2(I); % removes noise
    I3 = I2*10;
    BW = imbinarize(I3, graythresh(I3)); % binarize
    BW1 = bwpropfilt(BW, "area",1); % take largest area (breast area)
    masked = I2; masked (~BW1)=0;
    preprocessed = adapthisteq(masked); % enhance contrast
    Enhanced = preprocessed; %keep clean copy without pectoral muscle mask;

    %remove pectoral muscles
    [r, c]=size(BW1);
    box = regionprops(BW1,'BoundingBox'); %bounding box of breast region
    Bbox = box.BoundingBox;
    Bbox(1) = round(Bbox(1));
    Bbox(2) = round(Bbox(2));
    Bbox(3) = round(Bbox(3));
    Bbox(4) = round(Bbox(4));
    mask2 = ones(r-Bbox(2), Bbox(3));
    k = round(Bbox(3)/3);
    mask2 = triu (mask2, k); %corner defining pectoral muscles
    %mask2 = fliplr(mask2) %flip to left side depending on LEFT/RIGHT view
    mask1 = zeros (r-Bbox(2), Bbox (1));
    mask3 = zeros (r-Bbox(2), c-(Bbox(1) + Bbox(3)));
    mask = [mask1, mask2, mask3];
    pectmask = logical(mask); %convert to logical values
    test = imresize(pectmask, [r c]); %resize mask to be the same as preprocessed
    preprocessed(test) = 0;

    % Segmentation
    thresh = multithresh(preprocessed, 6); %Otsu's method
    seg = imquantize(preprocessed, thresh);
    lesion = seg > 6;
    se = strel('disk', 6); 
    lesion = imopen(lesion, se); %smoothing
    lesion = imclose(lesion, se);
    lesion = bwpropfilt(lesion, "area", [1000, 108000]); %regions between this size
    ROI = bwpropfilt(lesion, "area",1); % largest ROI
    preprocessed(~ROI) = 0

    % Crop

    stat = regionprops(ROI, 'centroid'); %find the centroid of ROIs
    row = round(stat.Centroid(2));
    column = round(stat.Centroid(1));
    [r, c] = size(preprocessed);
    if int16(row-150)>0 && int16(column-150)>0 && int16(row+149)<=r && int16(column+149)<=c %ensure crop area is within the image
        cropped = Enhanced(int16(row-150):int16(row+149), int16(column-150):int16(column+149)); % crop enhanced image ROI with size 300x300
        cropped = imresize(cropped, [32 32]); %resize cropped image to 32x32
        newfile = [name,'_crop.tif'];
        imwrite(cropped, newfile, 'tif') %save cropped image
    end
end
