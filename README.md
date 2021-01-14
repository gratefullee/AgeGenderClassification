# AgeGenderClassification

## Dataset
[Adience Dataset](https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification) 

around 19k+ of images: male/female, 8 different age groups 
- train set 70%
- test set 15%
- validation set 15%


![age_ratio](/img/ageratio.jpg){:height="50%" width="50%"}
![gender_ratio](/img/genderratio.jpg){:height="50%" width="50%"}

## VGG16 CNN Model

Gender Model 
- 10 epochs
- About 87% of accuracy
![cm_gender](/img/cm_gender.jpg){:height="50%" width="50%"}
![gender_examples](/img/gender_examples.jpg){:height="50%" width="50%"}



Age Model 
- 100 epochs 
- About 67% of accuracy
![cm_age](/img/cm_age.jpg){:height="50%" width="50%"}
![age_examples](/img/age_examples.jpg){:height="50%" width="50%"}


## Computer Vision

- Open CV Library
- Haar-Cascade Face Detection

![demo](/img/demo.gif)


## Conclusion / Future Works
- Overall the models' performance was good but I would definitely try out different models / different number of epochs, etc. 
- Dataset for Age group was not ideally balanced, so I would love to work on it more.


