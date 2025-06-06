# Guardian AI – Real-Time Security for Hassle-Free Cab Travel

Guardian AI is an intelligent, real-time vehicle surveillance system designed to ensure the safety of passengers in ride-hailing services. It leverages AI, facial recognition, and IoT technologies to monitor the cab interior and proactively detect threats or anomalies during travel.

## 🚀 Features

- Real-time video monitoring using ESP32-CAM
- Facial recognition for authorized passenger detection
- Anomaly detection using machine learning
- Emergency alert system with location and video feed
- Low-cost and energy-efficient design
- Cloud or local server storage integration

## 🛠 Technologies Used

- ESP32-CAM
- FTDI (Future Technology Devices International)
- Python
- OpenCV
- Machine Learning (TensorFlow/Keras)
- IoT
- Flask (for web app/dashboard)
- Local/Cloud Storage

## 📷 Hardware Requirements

- ESP32-CAM Module
- FTDI Converter Module
- Emergency Button (optional)
- Wi-Fi connection
- Power supply (Battery/USB)
- External sensors (optional – sound/motion)

## 🔧 Setup Instructions

1. **Install Arduino IDE** and set up ESP32 board support.
2. **Connect ESP32-CAM** to your PC using FTDI.
3. Upload the firmware that captures and streams video.
4. Connect the module to Wi-Fi and link it to the backend service.
5. Run the Python/Flask server for facial recognition and anomaly detection.
6. Integrate GPS and emergency button (optional).
7. Deploy and test in a real cab scenario.

## 📊 AI Capabilities

- **Facial Recognition**: Recognizes and matches passenger faces against a stored database.
- **Anomaly Detection**: Identifies sudden movements, aggression, or unauthorized access using trained models.

## 📩 Alerts & Notifications

- Sends real-time alerts to drivers, passengers, and the control room.
- Includes snapshot/video, location, and description of detected threat.

## 📁 Folder Structure
Guardian-AI/
├── esp32cam/
│ └── sketch.ino
├── server/
│ ├── app.py
│ ├── model/
│ └── templates/
├── data/
├── README.md
└── requirements.txt

yaml
Copy
Edit

## 👩‍💻 Contributors

- **Thireesha K** – Project Developer  
[LinkedIn](https://www.linkedin.com/in/thireesha-k-614b2224a) | [GitHub](https://github.com/Thireesha1)

---

## 📃 License

This project is for academic and demonstration purposes. For commercial use, please contact the contributor.

Documentation link : https://drive.google.com/file/d/1UBEKTM3SpI_lB6IK_nWy5ARlQ62jYw7b/view?usp=drivesdk

