import flask
from flask_cors import CORS
from flask import request, jsonify
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets import register_coco_instances
import cv2
import requests
import numpy as np

def score_image(predictor: DefaultPredictor, image_url: str):
    image_reponse = requests.get(image_url)
    image_as_np_array = np.frombuffer(image_reponse.content, np.uint8)
    image = cv2.imdecode(image_as_np_array, cv2.IMREAD_COLOR)

    # make prediction
    return predictor(image)

def prepare_pridctor():
    # register the data
    register_coco_instances("cleanOut_train", {}, "/app/CleanOut_data/train/train.json", "/app/CleanOut_data/train/")
    register_coco_instances("cleanOut_val", {}, "/app/CleanOut_data/test/test.json", "/app/CleanOut_data/test/")
    dataset_dicts_train = DatasetCatalog.get("cleanOut_train")

    # create config
    cfg = get_cfg()
    cfgFile = "/app/configs/cleanout_mask_rcnn_R_50_FPN_3x.yaml"
    cfg.merge_from_file(cfgFile)
    cfg.MODEL.DEVICE = "cpu"
    cfg.MODEL.WEIGHTS = "/app/weights/model_final_2000.pth"  # path to the model we just trained
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set a custom testing threshold
    cfg.MODEL.DEVICE = "cpu" # we use a CPU Detectron copy

    classes = MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes
    predictor = DefaultPredictor(cfg)
    print("Predictor has been initialized.")
    return (predictor, classes)

app = flask.Flask(__name__)
CORS(app)
predictor, classes = prepare_pridctor()

@app.route("/api/score-image", methods=["POST"])
def process_score_image_request():
    image_url = request.json["imageUrl"]
    scoring_result = score_image(predictor, image_url)

    instances = scoring_result["instances"]
    scores = instances.get_fields()["scores"].tolist()
    pred_classes = instances.get_fields()["pred_classes"].tolist()
    pred_boxes = instances.get_fields()["pred_boxes"].tensor.tolist()

    response = {
        "scores": scores,
        "pred_classes": pred_classes,
        "pred_boxes" : pred_boxes,
        "classes": classes
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
