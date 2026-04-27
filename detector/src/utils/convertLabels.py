import os
import sys
import cv2
import shutil

out_images = "detector/data/sintetic/images/"
out_labels = "detector/data/sintetic/labels/"

def test_print(folder, tmp, x_min, x_max, y_min, y_max):
    img = cv2.imread(os.path.join(folder, tmp))

    x1 = int(x_min * 1526)
    x2 = int(x_max * 1526)
    y1 = int(y_min * 862)
    y2 = int(y_max * 862)

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    cv2.imshow('Square', img)
    cv2.waitKey(0)

def test_printBound(folder, tmp, file):
    path = os.path.join(folder, file)

    with open(path, "r", encoding='utf-8') as f:
        original_label = f.read()
    f.close()

    points = original_label.split('zzz')[1].split(",")[1:]


    img = cv2.imread(os.path.join(folder, tmp))

    for point in points:
        coordinates = point.split(" ")

        newCoordinate = (int(float(coordinates[0][2:])), int(float(coordinates[1][2:])))
        cv2.circle(img, newCoordinate, radius=3, color=(0, 0, 255), thickness=-1)

    cv2.imshow('Square', img)
    cv2.waitKey(0)

def main(argv):
    folder = argv[1]
    tmp = ''
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            shutil.copy(os.path.join(folder, tmp), os.path.join(out_images, tmp))
        
            path = os.path.join(folder, file)

            with open(path, "r", encoding='utf-8') as f:
                original_label = f.read()
            f.close()

            coordinates = original_label.split("zzz")[0].split(" ")

            x_min = float(coordinates[1])
            x_max = float(coordinates[2])
            y_min = float(coordinates[3])
            y_max = float(coordinates[4])

            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2
            width = (x_max - x_min)
            height = (y_max - y_min)

            # test_printBound(folder, tmp, file)
            # continue

            # test_print(folder, tmp, x_min, x_max, y_min, y_max)
            # continue

            new_label = f'{coordinates[0]} {x_center} {y_center} {width} {height}'
            
            with open(os.path.join(out_labels, file), "w", encoding='utf-8') as f:
                f.write(new_label)
            f.close()
        tmp = file

if __name__ == "__main__":
    main(sys.argv)