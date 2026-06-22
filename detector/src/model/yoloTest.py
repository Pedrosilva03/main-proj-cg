import ultralytics
import cv2, os

testing_folder = "detector/data_split/test/images"

yaml_path = 'detector/data/data.yaml'
yolo_dataset_path = 'detector/data_split'

model_used = "runs/detect/train3/weights/best.pt"

def main():
    if not os.path.exists(yaml_path):
        print("Configuration file not found... Run training script")
        return
    
    if not os.path.exists(yolo_dataset_path):
        print("Dataset for YOLO not found... Run training script")
        return
    
    model = ultralytics.YOLO(model_used, task="detect")
    for image in os.listdir(testing_folder):
        results = model(os.path.join(testing_folder, image))

        annotated = results[0].plot()

        cv2.imshow("Detections", annotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Generate statistics
    model = ultralytics.YOLO(model_used)
    metrics = model.val(data='detector/data/data.yaml', split='test')
    print(metrics.results_dict)

if __name__ == "__main__":
    main()