# Fetch images from a video, adding 70% for training and 30% for testing

import cv2, os, sys, random

portion = 0.7

trainPath = "detector/data/real/images"
testPath = "detector/data/test"

def getFrames(videoPath):
    frames = []
    capture = cv2.VideoCapture(videoPath)
    success = True
    counter = 1
    while success:
        success, frame = capture.read()
        if counter % 40 == 0:
            frames.append(frame)
        counter += 1
    return frames

def main(argv):
    frames = getFrames(argv[1])
    split_point = int(len(frames) * portion)
    random.shuffle(frames)

    train = frames[:split_point]
    test = frames[split_point:]

    frameCounter = 1
    for trainFrame in train:
        cv2.imwrite(os.path.join(trainPath, "real_%d.png" % frameCounter), trainFrame)
        frameCounter += 1

    frameCounter = 1
    for testFrame in test:
        cv2.imwrite(os.path.join(testPath, "real_%d.png" % frameCounter), testFrame)
        frameCounter += 1

if __name__ == "__main__":
    main(sys.argv)