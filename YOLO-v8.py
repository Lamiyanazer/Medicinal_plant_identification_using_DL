from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')

model.train(data=r"C:\Users\lamiy\OneDrive\Desktop\Proj_MedPlants\Medicinal Leaf Dataset\Splittedimages", epochs=5)

metrics = model.val()