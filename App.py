from flask import Flask, render_template, Response
import cv2
import os
import time
from twilio.rest import Client
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Twilio config
TWILIO_ACCOUNT_SID = 'AC5d9fb4a99e8e1a825a1f54a46f16f44a'
TWILIO_AUTH_TOKEN = '368596ef9778edad71c47fe86f6f6ce6'
FROM_WHATSAPP_NUMBER = 'whatsapp:+14155238886'
TO_WHATSAPP_NUMBER = 'whatsapp:+917305395816'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Load reference images from folder
REFERENCE_FOLDER = os.path.join(os.path.dirname(__file__), 'img')

if not os.path.exists(REFERENCE_FOLDER):
    print(f"Error: Folder '{REFERENCE_FOLDER}' not found.")
    exit(1)

reference_images = []
image_names = []

orb = cv2.ORB_create()

for filename in os.listdir(REFERENCE_FOLDER):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        path = os.path.join(REFERENCE_FOLDER, filename)
        image = cv2.imread(path, 0)  # Load as grayscale
        kp, des = orb.detectAndCompute(image, None)
        if des is not None:
            reference_images.append((kp, des))
            image_names.append(filename)

last_alert_time = 0  # For rate-limiting alerts


def send_whatsapp_alert():
    try:
        message = client.messages.create(
            from_=FROM_WHATSAPP_NUMBER,
            body='🖐️ Alert: Emergency needed! Location: Dhaanish Chennai - https://maps.app.goo.gl/7EYTwbPNaf9m2BibA',
            to=TO_WHATSAPP_NUMBER
        )
        print(f'WhatsApp alert sent: SID={message.sid}')
    except Exception as e:
        print(f'Failed to send WhatsApp alert: {e}')


def is_match(des1, des2, threshold=10):
    if des1 is None or des2 is None:
        return False
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    return len(matches) >= threshold


def generate_frames():
    global last_alert_time

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            kp2, des2 = orb.detectAndCompute(gray_frame, None)

            for i, (kp1, des1) in enumerate(reference_images):
                if is_match(des1, des2):
                    if time.time() - last_alert_time > 30:
                        print(f'Match found: {image_names[i]}')
                        send_whatsapp_alert()
                        last_alert_time = time.time()
                    break  # Exit loop after first match

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
