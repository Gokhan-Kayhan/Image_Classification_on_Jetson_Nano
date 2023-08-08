# Image Classification on Jetson Nano


# Introduction

This project aims to classify Face Skin Diseases by using the power of deep learning concepts.

</br>

Firstly, custom **CNN Models** were used and then pretrained **MobileNet V2** was used with **Transfer Learning.** At the end, **Fine tuning** was done to increase the model performance. You can see how the accuracy on unused test images increases in each step.

</br>

The [model_training.ipynb](XXX) notebook can be taken as pipeline and used in different platforms. But it was designed to train the models with [*Intel Extension for TensorFlow*](https://intel.github.io/intel-extension-for-tensorflow/latest/get_started.html) on **Intel Developer Cloud** to accelerate training.

Later, the trained TensorFlow models are converted into **ONNX** and **TensorRT** formats and used in NVIDIA Jetson Nano to inference.

</br>

The dataset is based on [Dermnet dataset](https://www.kaggle.com/code/gauravduttakiit/class-dataset-face-skin-diseases/input) which has different types of skin diseases. But, in this project I used the smaller dataset which focus only [Face Skin Diseases.](https://www.kaggle.com/datasets/shubhamgoel27/dermnet)

---

</br>


# Installation
The project has 2 main part :  
- Intel Developer Cloud
- NVIDIA Jetson Nano

## Intel Developer Cloud
The necassary installation steps for **Intel Developer Cloud** and creating a suitable Kernel to be able to use **Intel Optimized TensorFlow**, can be found in the section [Intel Developer Cloud.](sections/installation_intel.md) 

You can simply run shell script files in that section and adjust everythings automatically. Alternatively, if you prefer, you can check [the details about Intel DevCloud](https://github.com/Gokhan-Kayhan/Image_Classification_on_Jetson_Nano/blob/main/sections/installation_intel.md#details-about-intel-devcloud) and apply the steps manually.

</br>

## NVIDIA Jetson Nano
The information about **Jetson Nano**, its setup and **Docker Image** which contains necassary packages can be found in the section [NVIDIA Jetson Nano.](sections/jetson_nano.md)
