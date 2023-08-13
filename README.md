# Image Classification on Jetson Nano


# Introduction

This project aims to classify Face Skin Diseases by using the power of deep learning concepts.

</br>

Firstly, custom **CNN Models** were used and then pretrained **MobileNet V2** was used with **Transfer Learning.** At the end, **Fine tuning** was done to increase the model performance. You can see how the accuracy on unused test images increases in each step.

</br>

The [model_training.ipynb](model_training.ipynb) notebook can be taken as pipeline and used in different platforms. But it was actually designed to train the models with [*Intel Extension for TensorFlow*](https://intel.github.io/intel-extension-for-tensorflow/latest/get_started.html) on **Intel Developer Cloud** to accelerate training.

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

You can simply run shell script file in that section and adjust everythings automatically. Alternatively, if you prefer, you can check [the details about Intel DevCloud](https://github.com/Gokhan-Kayhan/Image_Classification_on_Jetson_Nano/blob/main/sections/installation_intel.md#details-about-intel-devcloud) and apply the steps manually.


## NVIDIA Jetson Nano
The information about **Jetson Nano**, its setup and **[Docker Image](https://hub.docker.com/r/gokh44n/jetson-nano-project)** which contains necassary packages can be found in the section [NVIDIA Jetson Nano.](sections/jetson_nano.md)

---

</br>

# Model Training
After completing the above installation steps, you can continue with Model Training. You can simply follow the [model_training.ipynb](model_training.ipynb) notebook and run it cell by cell. It will read the images, applies some processings, creates the dataset, train the models and save them in TensorFlow SavedModel format.

I started with simple CNN and obtaied _55.6%_ accuracy on test images, then I improved this network and obtained _62.7%_
Later, I used MobileNet V2 with transfer learning and obtained _63.7%_ accuray. After the fine tuning, the accuracy of this model increased to _68.1%_

The more details about model training and converting TensorFlow models into ONNX format can be found in the section [Model Training.](sections/model_training.md)

---

</br>

# Run the Models on NVIDIA Jetson Nano

In Jetson Nano, you can convert **ONNX** models into **TensorRT** format and run both formats in Nano. I created another script file which handle the conversation process automatically. You can simply run it and test the Models in Nano by using [`run_onnx.py`](run_onnx.py) and [`run_tfrt.py`](run_tfrt.py)

You can find the details about TensorRT conversation and running the models in the section [Model Inference on Jetson Nano](sections/model_inference_on_nano.md)

---

</br>

# Youtube Video and NVIDIA Forum

You can watch the [Youtube video](https://youtu.be/qnGjDEGOqHQ) of the project and check the [NVIDIA Forum Post.]()
