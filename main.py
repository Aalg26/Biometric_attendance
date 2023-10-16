import cv2
import numpy as np
import face_recognition
import os
from emotions import mood  #  "mood" is a module for emotion detection based on deepfaces models
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import datetime
import time

# Initialize Firebase
cred = credentials.Certificate("biometric-9f3d4-firebase-adminsdk-ksj8f-f5c63c536e.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://biometric-9f3d4-default-rtdb.firebaseio.com/',
    'storageBucket': 'biometric-9f3d4.appspot.com'
})
bucket = storage.bucket()

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set webcam width
cap.set(4, 480)  # Set webcam height

# Load overlay image
overlay = cv2.imread('overlay/overlay.png')

# Load overlay modes
folder_modes_path = 'overlay/modes'
modes_path_list = os.listdir(folder_modes_path)
modes_list = []

for path in modes_path_list:
    modes_list.append(cv2.imread(os.path.join(folder_modes_path, path)))

# Load encoded worker names
file = open('names_known_encode.p', 'rb')
names_known_encode = pickle.load(file)
file.close()
faces_known_encode, worker_names = names_known_encode

# Initialize variables
mode = 0
counter = 0
name = 0
img_worker = []

while True:
    # Read from webcam
    success, frame = cap.read()
    frame = cv2.resize(frame, (550, 430))

    # Resize frame
    img_small = cv2.resize(frame, (0, 0), None, interpolation=cv2.INTER_LINEAR, fx=0.25, fy=0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    # Detect faces in the resized frame
    face_current_frame = face_recognition.face_locations(img_small)
    encode_current_frame = face_recognition.face_encodings(img_small, face_current_frame)

    for encodeFace, face_loc in zip(encode_current_frame, face_current_frame):
        matches = face_recognition.compare_faces(faces_known_encode, encodeFace)
        dist = face_recognition.face_distance(faces_known_encode, encodeFace)
        match_index = np.argmin(dist)

        if matches[match_index]:
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = 4 * y1, 4 * x2, 4 * y2, 4 * x1

            cv2.rectangle(frame, (x1 + 10, y1 + 10), (x2 + 10, y2 + 10), (0, 255, 0), 2)
            emotion = mood(frame)
            name = worker_names[match_index]
            emotion = mood(frame[y1 + 20:y2 + 20, x1 + 20:x2 + 20])

            if counter == 0:
                mode = 1
                overlay[105:105 + 480, 847:847 + 323] = modes_list[mode]
                counter = 1

    if counter != 0:
        if counter == 2:
            time.sleep(5)
            counter = 0

        if counter == 1:
            # Get the current date
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%d-%m-%Y")

            # Get worker info from Firebase
            worker_info = db.reference(f'Attendance {formatted_date}/{name}').get()
            ref = db.reference(f'Attendance {formatted_date}/{name}')

            # Update worker's emotion in Firebase
            worker_info['Feeling'] = emotion
            ref.child('Feeling').set(worker_info['Feeling'])

            # Download worker's image from Firebase Storage
            blob = bucket.get_blob(f'data/worker_id_img/{name}.png')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            img_worker = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

            # Determine mode based on emotion
            if emotion == 'angry':
                mode = 2
            elif emotion == 'happy':
                mode = 3
            elif emotion == 'neutral':
                mode = 4
            elif emotion == 'surprise':
                mode = 6
            else:
                mode = 5

            counter = 2
            overlay[105:105 + 480, 847:847 + 323] = modes_list[mode]
            cv2.putText(overlay, name, (950, 375), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            overlay[106:106 + 216, 900:900 + 216] = img_worker

    overlay[130:130 + 430, 135:135 + 550] = frame
    cv2.imshow('back', overlay)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    


 