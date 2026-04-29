import ultralytics
import os, yaml, random, shutil

yaml_path = 'detector/data/data.yaml'
classes_path = 'detector/data/sintetic/classes.txt'

yolo_dataset_path = 'detector/data_split'

split_ratio = 0.8

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
        'path': 'detector/data_split',
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
    if os.path.exists(yolo_dataset_path):
        print("Dataset for YOLO already exists")
        return
    
    # Create directories

    for type in ['train', 'val']:
        os.makedirs(os.path.join(yolo_dataset_path, type, "images"))
        os.makedirs(os.path.join(yolo_dataset_path, type, "labels"))

    # Data collection

    def collect_data(type):
        pairs = []
        image_folder = os.path.join(os.path.join("detector/data", type), "images")
        label_folder = os.path.join(os.path.join("detector/data", type), "labels")
        for image in os.listdir(image_folder):
            image_path = os.path.join(image_folder, image)
            label_path = os.path.join(label_folder, os.path.splitext(image)[0] + ".txt")

            pairs.append((image_path, label_path))
        return pairs

    sintetic_data = collect_data("sintetic")
    real_data = collect_data("real")

    total_data = sintetic_data + real_data
    random.seed(42)
    random.shuffle(total_data)

    split_index = int(len(total_data) * split_ratio)

    train_data = total_data[:split_index]
    val_data = total_data[split_index:]

    for train_element in train_data:
        shutil.copy(train_element[0], os.path.join(yolo_dataset_path, "train/images", os.path.basename(train_element[0])))
        shutil.copy(train_element[1], os.path.join(yolo_dataset_path, "train/labels", os.path.basename(train_element[1])))

    for val_element in val_data:
        shutil.copy(val_element[0], os.path.join(yolo_dataset_path, "val/images", os.path.basename(val_element[0])))
        shutil.copy(val_element[1], os.path.join(yolo_dataset_path, "val/labels", os.path.basename(val_element[1])))

    print("Dataset splitted and saved")

def main():
    create_yaml()
    split_data()

    model = ultralytics.YOLO("yolov8n.pt")

    model.train(data=yaml_path, epochs=15, imgsz=640)

if __name__ == "__main__":
    main()