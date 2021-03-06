FROM python:3.8-slim-buster

RUN apt-get update -y --no-install-recommends

# gcc compiler and opencv prerequisites
RUN apt-get -y --no-install-recommends install nano git build-essential libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
	python3-opencv ca-certificates python3-dev git wget sudo  \
	cmake ninja-build && \
  rm -rf /var/lib/apt/lists/*

# Detectron2 prerequisites
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install cython
RUN pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

# Detectron2 - CPU copy
RUN python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/index.html

# Development packages
RUN pip install flask flask-cors requests opencv-python



# Added after testing the flask code
WORKDIR /app
COPY web_api_cleanout.py /app/web_api_cleanout.py

WORKDIR /app/configs
COPY configs/cleanout_mask_rcnn_R_50_FPN_3x.yaml /app/configs/cleanout_mask_rcnn_R_50_FPN_3x.yaml


# Download the weights
WORKDIR /app/weights
COPY weights/model_final_3000.pth /app/weights/model_final_3000.pth

WORKDIR /app/CleanOut_data
COPY ./CleanOut_data/test/.  /app/CleanOut_data/test/
COPY ./CleanOut_data/train/.  /app/CleanOut_data/train/

RUN ls -la /app/

ENTRYPOINT ["python", "/app/web_api_cleanout.py"]
