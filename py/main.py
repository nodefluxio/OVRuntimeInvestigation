import os
import numpy as np
import cv2
import argparse

OPENVINO_AVAILABLE = True
try:
    from openvino.runtime import Core
    import openvino.properties.hint as hints
except:
    OPENVINO_AVAILABLE = False
import time

class OpenVinoEngine:
    def __init__(self, model_path, device="CPU"):
        if not OPENVINO_AVAILABLE:
            raise RuntimeError("OpenVINO is not available, please install 'openvino==2022.1.0'")
        self.model_path = model_path
        self.device = device

        core = Core()
        model = core.read_model(self.model_path)
        self.model = core.compile_model(model, self.device)
        self.infer_req = self.model.create_infer_request()

    def infer_det(self, image, score_thresh, iou_thresh):
        input_feed = {
            "input": image,
            "iou_threshold": np.array([iou_thresh], dtype=np.float32),
            "score_threshold": np.array([score_thresh], dtype=np.float32)
        }

        result = self.infer_req.infer(inputs=input_feed)
        result = [x for x in result.values()]
        return result
    

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--device",
        "-d",
        type=str,
        default="CPU",
        help="selected device (CPU, GPU), default: CPU",
    )
    args = parser.parse_args()
    device = args.device
    device = device.upper()

    ov = OpenVinoEngine(model_path="models/model.onnx", device=device)
    ori_image = cv2.imread("images/face.jpg")
    image = np.expand_dims(cv2.resize(ori_image, (640, 640)), axis=0)
    latency = []
    for i in range(1):
        st = time.time()
        results_det = ov.infer_det(image, 0.9, 0.4)
        latency.append(time.time() - st)
        time.sleep(0.0001)
    
    try:
        results_det = results_det[0][0][0]
        cv2.rectangle(ori_image, (int(results_det[0]*ori_image.shape[1]), int(results_det[1]*ori_image.shape[0])),
                    (int(results_det[2]*ori_image.shape[1]), int(results_det[3]*ori_image.shape[0])), (255,0,0), 2)
        print (f"Output face detection ={results_det}, Running on {device} device, FPS={1/np.mean(np.array(latency))}")
    except:
        print ("No face detected")
        print (f"Output face detection ={[]}, Running on {device} device, FPS={1/np.mean(np.array(latency))}")
    
    cv2.imwrite("data/result_image.jpg", ori_image)
    
