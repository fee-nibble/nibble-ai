from darknet.darknet_images import check_batch_shape
from darknet import *

def find_ed():
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

def change_braille(num):
    braille = [14, 1, 5, 3, 11, 9, 7, 15, 13, 6]
    return braille[int(num)]

def decode_braile(num):
    return list(map(int, format(num, 'b').zfill(6)))


ed = 211215 # 유통기한 ['2', '1', '1', '2', '1', '5'] -> 5 1 1 5 1 9
c_braille = list(map(lambda x: change_braille(x), list(str(ed))))
print(c_braille)
d_braille = list(map(lambda x: decode_braile(x), c_braille))
print(d_braille)