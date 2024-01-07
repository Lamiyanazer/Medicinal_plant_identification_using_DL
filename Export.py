from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-cls.pt')  # load an official model
model = YOLO(r'C:\Users\lamiy\OneDrive\Desktop\Proj_MedPlants\Medicinal Leaf Dataset\runs\classify\train3\weights\best.pt')  # load a custom trained model

# Export the model
model.export(format='onnx')




