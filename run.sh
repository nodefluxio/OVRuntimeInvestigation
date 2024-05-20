# /bin/sh

echo "================= RUN CPU ======================="
echo "Running Python Runtime with docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 --device CPU "
docker run --rm -it docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 --device CPU

echo "================= RUN GPU ======================="

echo "Running Python Runtime with docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 --device GPU "
docker run --device=/dev/dri --rm -it docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 --device GPU
