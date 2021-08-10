from darknet import *
import cv2
net = load_network("cfg/yolov3_training.cfg", "data/obj.data", "backup/nibble.weights")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # detect 'ED'
    detections = detect_image(net[0], net[1], nparray_to_image(frame))
    # return img with boxes
    frame = draw_boxes(detections, frame, net[2])
    # show frame
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()