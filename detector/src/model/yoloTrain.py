import ultralytics
import os, yaml

yaml_path = 'detector/data/data.yaml'
classes_path = 'detector/data/sintetic/classes.txt'

def create_yaml():
    if os.path.exists(yaml_path):
        print("Skipping configuration: Config file already exists")
        return
    
    with open(classes_path, "r", encoding='utf-8') as f:
        parsed_classes = {}
        classes = f.read().split("\n")
        i = 0
        for classs in classes:
            parsed_classes[i] = classs
            i+=1
        number_of_classes = len(parsed_classes.keys())
    
    yaml_content = {
        'path': '/detector/data_split',
        'train': 'train/images',
        'val': 'val/images',
        'nc': number_of_classes,
        'names': parsed_classes
    }

    with open(yaml_path, "w", encoding='utf-8') as f:
        yaml.dump(yaml_content, f, sort_keys=False)
    f.close()

    print("Configuration file created")

def split_data():
    pass

def main():
    create_yaml()
    return
    split_data()

    model = ultralytics.YOLO("yolov8n.pt")

    model.train(data=yaml_path, epochs=50, imgsz=640)

if __name__ == "__main__":
    main()