import numpy as np
import cv2
import dlib

class FaceDetection:
    
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        
    def faceDetection(self,img):
        
        if type(img) is str:
            img = cv2.imread(img)
        
        return self.detector(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

class FaceDescription:
    
    def __init__(self, landmarksPath, recModelPath):
        self.landmarks = dlib.shape_predictor(landmarksPath)
        self.recModel = dlib.face_recognition_model_v1(recModelPath)

    def faceDesctiption(self,img, dets = None):
        
        if type(img) is str:
            img = cv2.imread(img)
            dets = None
            
        if dets == None:
            dets = FaceDetection().faceDetection(img)
            
        faces = []

        for d in dets:
            shape = self.landmarks(img, d)
            faces.append(np.array(self.recModel.compute_face_descriptor(img, shape)))

        return faces