from PIL import Image
import shutil

import json
import os
import argparse

def convert_coco_to_yolo_seg(coco_root, output_dir, split='train'):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', split), exist_ok=True)
    with open(os.path.join(coco_root, 'annotations', split+'.json')) as f:
        coco = json.load(f)

    img_ids = {img['id']: img for img in coco['images']}
    annotations = coco['annotations']

    for img_id in img_ids:
        annotation_string = ""
        annotations_for_img = [a for a in annotations if a['image_id'] == img_id]

        for annotation in annotations_for_img:
            annotation_string += "0 " + " ".join([str(x/256) for x in annotation['segmentation'][0]]) + "\n"
        
        filename = img_ids[img_id]['file_name'].split('.')[0]
        with open(os.path.join(output_dir, 'labels', split, f"{filename}.txt"), 'w') as f:
            f.write(annotation_string)

    for img_id, img in img_ids.items():
        shutil.copy(
            os.path.join(coco_root, split, img['file_name']),
            os.path.join(output_dir, 'images', split, img['file_name'])
        )
        
        
    yaml_path = os.path.join(output_dir, 'yolo_root.yaml')
    abs_path = os.path.abspath(output_dir)
    
    # Create YAML content
    yaml_content = f"""
path: {abs_path}
train: ./images/train
val: ./images/val

names:
    0: location
"""
    
    with open(yaml_path, 'w') as f:
        f.write(yaml_content)
 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--coco_root', type=str, required=True)
    parser.add_argument('--yolo_dataset_output_dir', type=str, required=True)    
    args = parser.parse_args()
    
    convert_coco_to_yolo_seg(args.coco_root, args.yolo_dataset_output_dir, split='train')
    convert_coco_to_yolo_seg(args.coco_root, args.yolo_dataset_output_dir, split='val')
    
if __name__ == "__main__":
    main()
