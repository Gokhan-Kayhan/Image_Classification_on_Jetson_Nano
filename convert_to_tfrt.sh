
/usr/src/tensorrt/bin/trtexec --onnx=/home/docker_transfer/onnx_models/onnx_model1.onnx --saveEngine=/home/docker_transfer/tfrt_models/model1.trt
echo "-------------------------Model1 converted-------------------------"


/usr/src/tensorrt/bin/trtexec --onnx=/home/docker_transfer/onnx_models/onnx_model2.onnx --saveEngine=/home/docker_transfer/tfrt_models/model2.trt
echo "-------------------------Model2 converted-------------------------"


/usr/src/tensorrt/bin/trtexec --onnx=/home/docker_transfer/onnx_models/onnx_mobilenet.onnx --saveEngine=/home/docker_transfer/tfrt_models/mobilenet.trt
echo "-------------------------MobileNet_Model converted-------------------------"


/usr/src/tensorrt/bin/trtexec --onnx=/home/docker_transfer/onnx_models/onnx_mobilenet_fine.onnx --saveEngine=/home/docker_transfer/tfrt_models/mobilenet_fine.trt
echo "-------------------------MobileNet_Fine_Model converted-------------------------"

