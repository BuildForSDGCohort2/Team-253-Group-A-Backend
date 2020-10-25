# Notes

## Training

To train the model we use the pre-trained weights of the `Mask RCNN ResNet 50 FPN 3X` without augmenting the data at first. It was trained for 1k, 2K then 3K.   
The best result in this bacth tested on the validation set is the model trained on 3k epoch and scored an `AP(bbox) = 32.171` and `AP(segmentation) = 31.201`.  
If you want to check the code please open the `Augment_&_Train_Detectron2_on_CleanOut.ipynb` notebook using Colab.

Because we had less data than usually required to get good results we tried to augment it by performing horizontal and vertical random flips. At first the results where improving but by 3k epoch they got worse.  
Best obtained results where after training for 2k epoch: `AP(bbox) = 31.933` and `AP(segmentation) = 31.400`.  
Please check the `Train_Detectron2_on_CleanOut.ipynb` notebook using Colab for further details.  

## Best Results

The best results are the ones produced by the model without data augmentation that has been trained for 3k epoch.  
**Scores:** `AP(bbox) = 32.171` and `AP(segmentation) = 31.201`.  
**Weights file:** [Link](https://drive.google.com/file/d/1Y4YeSB3mQ0PN9zuAdSPKtPV1jNpYa_IX/view?usp=sharing).  
**Data files:** [Link](https://drive.google.com/file/d/1JpLqAvIbk7BpoNq7jj1_j-nx7892t_p3/view?usp=sharing). 
