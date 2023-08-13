# region imports
import os
import cv2
import time
import json
import pathlib
import warnings
import numpy as np
import tensorrt as trt
warnings.filterwarnings("ignore")
# endregion
#--------------------------------------------------



# region variables
tfrt_model_save_path = "/home/docker_transfer/tfrt_models/mobilenet_fine.trt"
		    
# We analyze 1 image at each time
BATCH_SIZE=1

# FP32 is the default training precision of most frameworks
PRECISION = np.float32

N_CLASSES = 5     
# endregion
#--------------------------------------------------



# Load Model
trt_model = ONNXClassifierWrapper(tfrt_model_save_path, [BATCH_SIZE, N_CLASSES], 
target_dtype = PRECISION)
#--------------------------------------------------



# region warmup
# TRT Model requires to warmup and then available for prediction
batched_input = np.zeros((8, 160, 160, 3), dtype=np.float32)
N_warmup_run = 50

for i in range(N_warmup_run):
  preds = trt_model.predict(batched_input)
#endregion
#--------------------------------------------------



#region model inference
# To run the model on test folder and make the predictions
def model_inference_on_test_images(folder_path, loaded_model):
    img_height, img_width = (160,160)
    class_labels = []


    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Loop through each file in the list
    for file_name in file_list:
        if file_name.endswith(".jpg"):
            # Construct the full path of the image
            image_path = os.path.join(folder_path, file_name)

            # Read the image using OpenCV
            img = cv2.imread(image_path)

            img.resize(img_height, img_width)

            data = json.dumps({'data': img.tolist()})
            data = np.array(json.loads(data)['data']).astype('float32')

            data = data/ 255.0

            prediction = loaded_model.predict(data)
            score = int(np.argmax(prediction))
            class_labels.append(score)
#endregion
#--------------------------------------------------



#region test image folders
totaltime = 0
start = time.time()

test_images_folder0 = "/home/docker_transfer/DATA/testing/Acne/"
test0_predicted_labels = model_inference_on_test_images(test_images_folder0,trt_model)

test_images_folder1 = "/home/docker_transfer/DATA/testing/Actinic Keratosis/"
test1_predicted_labels = model_inference_on_test_images(test_images_folder1,trt_model)

test_images_folder2 = "/home/docker_transfer/DATA/testing/Basal Cell Carcinoma/"
test2_predicted_labels = model_inference_on_test_images(test_images_folder2,trt_model)

test_images_folder3 = "/home/docker_transfer/DATA/testing/Eczemaa/"
test3_predicted_labels = model_inference_on_test_images(test_images_folder3,trt_model)

test_images_folder4 = "/home/docker_transfer/DATA/testing/Rosacea/"
test4_predicted_labels = model_inference_on_test_images(test_images_folder4,trt_model)

end = time.time()

totaltime = end - start
#endregion
#--------------------------------------------------



print("##### Training was completed in ",totaltime," seconds. #####")
print("##### 1 Image is analyzed in ",totaltime/185.0," seconds. #####")

