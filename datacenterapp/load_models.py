from ultralytics import YOLO

cabinet_model = YOLO("datacenterapp/models/datacenter.pt")
fire_model = YOLO("datacenterapp/models/fire_n.pt")
print('Models Loaded')

# Rest of your program...
