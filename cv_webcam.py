import cv2
import math
import argparse
import tensorflow as tf
import numpy as np

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes


parser=argparse.ArgumentParser()
parser.add_argument('--image')

args=parser.parse_args()

faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
ageModel=tf.keras.models.load_model('model/age_class.h5')

genderModel=tf.keras.models.load_model('model/gender_class.h5')



faceNet=cv2.dnn.readNet(faceModel,faceProto)
gender_list  = ['female', 'male']
age_list = ['15-20', '48-53', '25-32', '38-43', '0-2', '8-13', '4-6', '60+']
width, height = 224,224
dsize = (width,height)
img = cv2.imread('menow.jpg')

video=cv2.VideoCapture(args.image if args.image else 0)
padding=20
while cv2.waitKey(1)<0:
    hasFrame,frame=video.read()
    if not hasFrame:
        cv2.waitKey()
        break

    resultImg,faceBoxes=highlightFace(faceNet,frame)
    if not faceBoxes:
        print("No face detected")
        
    if faceBoxes==[]:
        cv2.putText(resultImg, 'detecting', (0,0), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
        print("detecting")

    else:
        gender = gender_list[np.argmax(genderModel.predict(np.expand_dims(cv2.resize(frame,dsize),axis=0)))]
        age = age_list[np.argmax(ageModel.predict(np.expand_dims(cv2.resize(frame,dsize), axis=0)))]
        print (gender+ ", " +age)

        cv2.putText(resultImg, f'{gender}, {age}', (faceBoxes[0][0],faceBoxes[0][1]-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2, cv2.LINE_AA)

        cv2.imshow("Detecting age and gender", resultImg)

