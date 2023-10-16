import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import datetime

cred = credentials.Certificate("biometric-9f3d4-firebase-adminsdk-ksj8f-f5c63c536e.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://biometric-9f3d4-default-rtdb.firebaseio.com/',
    'storageBucket':'biometric-9f3d4.appspot.com'
})

folder_path = 'data/worker_id_img'
path_worker_list = os.listdir(folder_path)


img_list = []
worker_names = []

for worker in path_worker_list:

    img_list.append(cv2.imread(f'{folder_path}/{worker}'))
    
    worker_names.append(os.path.splitext(worker)[0])

    file_name = f'{folder_path}/{worker}'
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)

def Encoder(img_list):
    encode_list = []
    for img in img_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)

    return encode_list

print('Encoding all workers faces')

faces_known_encode = Encoder(img_list)
names_known_encode = [faces_known_encode,worker_names]
print('Encoding completed succesfully')


file = open('names_known_encode.p', 'wb')
pickle.dump(names_known_encode,file)
file.close()
print('file saved')

