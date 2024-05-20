# OVRuntimeInvestigation

## Libraries
- Openvino 2024.1.0
- Openvino-dev 2024.1.0

## How to Build
```
bash build.sh
```

## How to Run
```
bash run.sh
```

## Log
### [May 20, 2024]
- OpenVino Runtime on CPU was working well, obtain correct result
- Issue: OpenVino Runtime on GPU got no detection
```bash
================= RUN CPU =======================
Running Python Runtime with docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 --device CPU 
Output face detection =[0.50217533 0.1292618  0.76857924 0.5328683  0.9968176  0.
 0.5994877  0.3277501  0.695311   0.27297825 0.69694334 0.35322013
 0.66372544 0.45049083 0.741006   0.40392226], Running on CPU device, FPS=56.54301082516615

================= RUN GPU =======================
Running Python Runtime with docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 --device GPU 
No face detected
Output face detection =[], Running on GPU device, FPS=186.61256451325858
```