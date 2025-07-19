from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(
    data='C:/Users/Thilipan/Desktop/face_dataset/data.yaml', 
    epochs=50,
    imgsz=640,
    batch=8
)

trained_model = YOLO('runs/detect/train/weights/best.pt')

results = trained_model.predict(
    source=r"C:\Users\Thilipan\Desktop\face_dataset\images\dinesh_1_jpeg.rf.00d3c8dc05c81f74e8f1fec09f5e5634.jpg",  
    conf=0.5
)

results.show()
