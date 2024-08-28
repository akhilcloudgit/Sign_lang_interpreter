import os
import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode =True,  min_detection_confidence = 0.3)
DATA_DIR = './data'

data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    # Create the full path for the directory
    dir_path = os.path.join(DATA_DIR, dir_)
    
    # Check if the item is a directory before processing
    if os.path.isdir(dir_path):
        for img_path in os.listdir(dir_path):
            data_aux = []
            # Create the full path for the image file
            img_file_path = os.path.join(dir_path, img_path)
            
            # Check if the item is a file before processing
            if os.path.isfile(img_file_path):
                img = cv2.imread(img_file_path)
                if img is not None:
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    results = hands.process(img_rgb)
                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            for i in range(len(hand_landmarks.landmark)):
                                x = hand_landmarks.landmark[i].x
                                y = hand_landmarks.landmark[i].y
                                data_aux.append(x)
                                data_aux.append(y)

                                
                        data.append(data_aux)
                        labels.append(dir_)
f = open('data.pickle','wb')
pickle.dump({'data':data , 'labels':labels},f)
f.close()
