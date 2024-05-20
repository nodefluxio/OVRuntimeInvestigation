FROM openvino/ubuntu22_dev_mtl:2024.1.0

USER root
WORKDIR /app
COPY py/* /app
COPY models/* /app/models/
COPY images/* /app/images/
RUN pip install openvino==2024.1.0 openvino-dev==2024.1.0 
ENTRYPOINT [ "python3", "-u", "/app/main.py" ]