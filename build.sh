# /bin/sh

echo "Building Python Runtime docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0"
docker build -f dockerfiles/ubuntu22_dev_mtl_py.Dockerfile -t docker.io/openvino/ubuntu22_dev_mtl_py_app:2024.1.0 .
