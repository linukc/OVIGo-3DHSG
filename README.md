## Dataset
We provide the dataset in coco-like format consisting of 547 manually selected scenes from [Scannet++v2 Dataset](https://kaldir.vc.in.tum.de/scannetpp/). Scenes were annotated using an automatic method and then manually corrected. The images and annotations have already been resized to square dimensions.

## Location detection training

To reproduce YOLO location detection training process, place dataset folder `coco_locations`, which we provide, in the root of this repository. Then run the training script: 

```bash
bash train_yolo.sh
```

This will create a new directory `yolo_locations_dataset` which contains the dataset in YOLO format and then start YOLO training process. 