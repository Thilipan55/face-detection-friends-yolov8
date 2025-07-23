# Friends Face Detection using YOLOv8

This project uses YOLOv8 for detecting and identifying faces of six friends from a custom dataset. It includes data preparation, training, and webcam-based inference.

## Project Structure

- images/        - Training images
- labels/        - YOLO labels for images
- train_batch/   - Sample detections from training data
- val_batch/     - Sample detections from validation data
- metrics/       - Training results and metrics
- data.yaml      - Dataset configuration for YOLO
- train_data.py  - Script for training and running detection
- requirements.txt

## How to Run

Install requirements:
pip install -r requirements.txt

yaml
Copy
Edit

Run training:
python train_data.py

markdown
Copy
Edit

Run webcam detection is handled inside `train_data.py`.

## Sample Outputs

Example detections on training and validation images are provided in `train_batch/` and `val_batch/`. Training metrics are in `metrics/`.

## Requirements
- Python 3.13
- YOLOv8 (Ultralytics)
- OpenCV