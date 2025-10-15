
import os
import time
#from gtts import gTTS
import cv2
import numpy as np
import pyttsx3
# import multiprocessing
# import keyboard
def speak(text):
    if cv2.waitKey(1) & 0xFF == 27:
        return
    speak_engine = pyttsx3.init()
    voices = speak_engine.getProperty('voices')
    speak_engine.setProperty('voice', voices[1].id)
    speak_engine.setProperty('rate', 180)
    speak_engine.say(text)
    speak_engine.runAndWait()
    speak_engine.stop()

# def say(phrase):
#     if __name__ == "__main__":
#         p = multiprocessing.Process(target=speak, args=(phrase,))
#         p.start()
#         while p.is_alive():
#             if keyboard.is_pressed('esc'):
#                 p.terminate()
#             else: continue
#         p.join()

'''
Text-to-Speech Module is defined above
Capture Screen and the Rest of the Code Comes Below
'''
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("There's some Problem with your WebCam")

cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)


net = cv2.dnn.readNet("yolov3.weights","yolov3.cfg")
classes = []
with open("coco.names","r") as f:
    classes = f.read().splitlines()
# print(classes)

while True:

    success, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    """
    for b in blob:
        for n, img_blob in enumerate(b):
            cv2.imshow(str(n), img_blob)
    """
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layersOutput = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layersOutput:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
            else:
                continue

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(class_ids) != 0:
        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(len(boxes), 3))

        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color= color, thickness= 2)
            cv2.putText(img, label + " : " + confidence, (x, y + 20), font, 2, (0, 255, 0), 2)
            # cv2.putText(img, label.upper(), (x, y + 20),
            #             font, 0.8, (0, 255, 0), 2)
            # cv2.putText(img, str(round(confidence * 100, 2)), (x + 200, y + 20),
            #             font, 0.8, (0, 255, 0), 2)


            if float(confidence)>0.8:
                text = label + " is approaching"
                print(text)
                # speak(text)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
    cv2.imshow("Output", img)
    # if storage 1ms and press esc exit break
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release
cv2.destroyAllWindows()
