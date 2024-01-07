from ultralytics import YOLO

model = YOLO(r'C:\Users\lamiy\OneDrive\Desktop\Proj_MedPlants\Medicinal Leaf Dataset\runs\classify\train3\weights\best.onnx',task='classify')

#prediction

p1=model.predict(r"C:\Users\lamiy\OneDrive\Desktop\Proj_MedPlants\Mexican Mint\Mex_m5.jpg",save=True, imgsz=224, conf=0.5)