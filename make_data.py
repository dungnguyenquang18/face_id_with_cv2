import cv2
import pandas as pd
import os
from matplotlib import pyplot as plt
import uuid
id=input()
id_path=os.path.join('data',id)
os.makedirs((id_path))
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = frame[120:120 + 250, 250:250 + 250, :]
    if cv2.waitKey(1) == ord('a'):
        imgname = os.path.join(id_path, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)
    cv2.imshow('Image Collection', frame)
    if cv2.waitKey(1) == ord('q'): break

cap.release()

cv2.destroyAllWindows()