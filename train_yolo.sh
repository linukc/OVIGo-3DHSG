#/bin/bash

echo "Sonverting COCO to YOLO format..."
python3 convert_coco_to_yolo.py --coco_root coco_locations/ --yolo_dataset_output_dir yolo_locations_dataset/

echo "Starting YOLO training..."
yolo segment train data=yolo_locations_dataset/yolo_root.yaml model=yolo11m-seg.pt epochs=300 imgsz=256 plots=True batch=-1