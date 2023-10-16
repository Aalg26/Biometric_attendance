import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

# Initialize Firebase with your credentials
cred = credentials.Certificate("biometric-9f3d4-firebase-adminsdk-ksj8f-f5c63c536e.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://biometric-9f3d4-default-rtdb.firebaseio.com/'
})

# Get the current date and format it as "dd-mm-yyyy"
current_date = datetime.date.today()
formatted_date = current_date.strftime("%d-%m-%Y")

# Create a reference to the Firebase database for today's date
ref = db.reference(f'Attendance {formatted_date}')

# Define the data to be stored in the database
data = {
    'Noah': {
        'Age': 70,
        'Feeling': 'Sad'
    },
    'Oliver': {
        'Age': 18,
        'Feeling': 'Happy'
    },
    'Olivia': {
        'Age': 38,
        'Feeling': 'Happy'
    }
}

# Iterate over the data and set it in the Firebase database
for key, value in data.items():
    ref.child(key).set(value)
