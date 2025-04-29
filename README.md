## Location detection training

To reproduce YOLO location detection training process, place dataset folder 'coco_locations', which we provide, in the root of this repository. Then run the training script: 

```bash
bash train_yolo.sh
```

This will create new directory `yolo_locations_dataset` which contains dataset in YOLO format and then start YOLO training process. 