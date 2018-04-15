import numpy as np
import cv2
import dlib
import database
import models
import os
import matplotlib.pyplot as plt
fdet = models.FaceDetection()
fdes = models.FaceDescription('data/model_weights/LandmarkFace.dat', 'data/model_weights/ResNetFace.dat')

AGS_model = models.WideResNetCreater()()
img_size = 64

AGS_model.load_weights(os.path.join("data/model_weights/", "weights.18-4.06.hdf5"))

def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
               font_scale=1, thickness=2):
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x, y = point
    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y), (255, 0, 0), cv2.FILLED)
    cv2.putText(image, label, point, font, font_scale, (255, 255, 255), thickness)

source = 'data/test.mp4'

db = database.DataBase('inarea.json')
cap = cv2.VideoCapture(source)

facesV = []

i = 0
tmp = 0
t = 0
j  = 0

while cap.isOpened():

    ret, img = cap.read()
    for j in range(5):
    	_, _ = cap.read()
    try:
        #img = cv2.resize(img, (480 * 2,270 * 2))
        img_h, img_w, img_ch = np.shape(img)
    except:
        break

    dets = fdet(img)

    facesV = fdes(img, dets = dets)

    input_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = np.empty((len(dets), img_size, img_size, 3))

    if len(dets) > 0:

        for i, d in enumerate(dets):
            x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()
            xw1 = max(int(x1 - 0.4 * w), 0)
            yw1 = max(int(y1 - 0.4 * h), 0)
            xw2 = min(int(x2 + 0.4 * w), img_w - 1)
            yw2 = min(int(y2 + 0.4 * h), img_h - 1)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

            faces[i,:,:,:] = cv2.resize(img[yw1:yw2 + 1, xw1:xw2 + 1, :], (img_size, img_size))


        results = AGS_model.predict(faces)
        predicted_genders = results[0]
        ages = np.arange(0, 101).reshape(101, 1)
        predicted_ages = results[1].dot(ages).flatten()


        ages_label = ['C' for i in range(len(dets))]

        for i, d in enumerate(dets):

            if predicted_ages[i] < 18:
                ages_label[i] = 'C'

            elif 18 <= predicted_ages[i] < 30:
                ages_label[i] = 'Y'

            elif 30 <= predicted_ages[i] < 55:
                ages_label[i] = 'A'

            else:
                ages_label[i] = 'O'

            label = "{}-{}".format(ages_label[i],"F" if predicted_genders[i][0] > 0.5 else "M")
            draw_label(img, (d.left(), d.top()), label)
            if label[2] == 'F':
            	check, index = db._input({'vector':facesV[i], 'age':ages_label[i], 'gender':'F','frame':t})

            else:
            	check, index = db._input({'vector':facesV[i], 'age':ages_label[i], 'gender':'M', 'frame':t})

    t+=1  
    cv2.imshow('capture', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
db.getstatistic(t, 7)
cv2.destroyAllWindows()
cap.release()

import webbrowser
import web
web.main()
webbrowser.open_new('localhost:8082')