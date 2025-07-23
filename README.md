Friends Face Detection using YOLOv8
This project uses YOLOv8 to detect and classify faces of characters from the Friends TV show.

 Project Structure
graphql
Copy
Edit
friends-face-detection-yolov8/
│
├── images/                 # Raw dataset images
├── labels/                 # YOLO-format label files
├── metrics/                # Evaluation outputs (e.g., val batches)
├── train_batch/           # Training image samples with predicted boxes
├── val_batch/             # Validation image samples with predicted boxes
├── data.yaml              # YOLO config file (class names, paths)
├── train_data.py          # Dataset preprocessing script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

 Features
Trained on a custom dataset of Friends characters

YOLOv8 model fine-tuned with labeled face data

Clean structure and modular code for retraining and extension

 How to Run
1. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
2. Train the model
bash
Copy
Edit
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
📊 Dataset
Collected images of main characters from Friends

Labeled using Roboflow in YOLO format

Split into training and validation sets

🔧 Future Improvements
Add more characters and samples

Improve accuracy using deeper YOLO variants (e.g., yolov8m)

Auto-labeling pipeline for bulk images

Add webcam-based real-time detection

