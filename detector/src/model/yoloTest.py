import ultralytics
import cv2, os

testing_folder = "detector/data/test"

def main():
    model = ultralytics.YOLO("runs/detect/train5/weights/best.pt", task="detect")
    for image in os.listdir(testing_folder):
        results = model(os.path.join(testing_folder, image))

        annotated = results[0].plot()

        cv2.imshow("Detections", annotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()