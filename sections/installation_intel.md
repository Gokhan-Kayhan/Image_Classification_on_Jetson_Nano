# Intel Developer Cloud

Since I don't have suitable Intel Hardware, I have made all the test on Intel Developer Cloud. We can [sign up](https://devcloud.intel.com/oneapi/home/) and use the Intel oneAPI toolkits and Intel hardwares free for 120 days.


After registration, we should connect to DevCloud. There are two ways :  
1 - There is a part **"Connect with JupyterLab\"** at the end of this [website](https://devcloud.intel.com/oneapi/get_started/). By simply clicking _"Launch JupyterLab"_, we can connect to Intel DevCloud.

2 - From Terminal via **SSH**
As seen in the below picture, we should choose our operating system and download private SSH key file. For the sake of simplicity, I suggest to follow instructions in _"Automated Configuration"_ section.

<p align="center">
<img src="figures/connect2devcloud.png"  width="75%" height="75%" >
</p>

---

</br>

# Create Virtual Environments and Kernel from Shell Script File

I will continue with JupyterLab since it is easier to visualize. 

I created 2 shell script files which adjust everythings automatically(installing the packages, creating the kernel and etc.) Firstly, you can create a folder and put all necassary files as in the figure below and you can run the `.sh`files in terminal like this : _(Do not forget to change the directory where the script is located)_

<p align="center">
<img src="figures/sh file.png" width="75%" height="75%">
</p>

Make the Script Executable
```
chmod +x training_env.sh
```

Run the Script
```
./training_env.sh
```

</br>
</br>

We need to create 2 different virtual environments : 

- training_env : Responsible for Model training with Intel Tensorflow Extension.
- transform_onnx_env : Responsible for converting TensorFlow model into ONNX format.

Because, Intel Tensorflow Extension is only compatible with TensorFlow v2.13.0 according to its [documentation](https://github.com/intel/intel-extension-for-tensorflow/blob/main/docs/install/install_for_cpu.md#install-tensorflow)

But the `tf2onnx` library which is used to convert saved TensorFlow model into ONNX format, does not work with this version. At the time I created this document, it was only working with TensorFlow v2.12.0

Therefore second virtual environment is used only to convert TensorFlow model into ONNX format.


