// Define pin numbers
const int mq2Pin = A0;        // MQ-2 sensor connected to analog pin A0
const int buzzerPin = 3;      // Buzzer connected to digital pin 3
const int buttonPin = 7;      // Push button connected to digital pin 7

// Threshold for fire detection
const int fireThreshold = 1500;  // Adjust this value based on calibration

// Variables for button handling
bool buzzerManualState = false;  // Tracks manual toggle state
bool lastButtonState = LOW;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50; // milliseconds

void setup() {
  Serial.begin(9600);

  pinMode(buzzerPin, OUTPUT);
  digitalWrite(buzzerPin, LOW);

  pinMode(mq2Pin, INPUT);
  pinMode(buttonPin, INPUT_PULLUP);  // Using internal pull-up resistor
}

void loop() {
  // Read MQ-2 sensor value
  int mq2Value = analogRead(mq2Pin);
  Serial.print("MQ-2 Value: ");
  Serial.println(mq2Value);

  // Read the state of the button (invert because of INPUT_PULLUP)
  bool reading = !digitalRead(buttonPin);  // true when pressed

  // Check for button state change with debounce
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // If the button was pressed, toggle buzzerManualState
    if (reading && !buzzerManualState) {
      buzzerManualState = true;
      Serial.println("Button Pressed: Buzzer ON");
    } else if (reading && buzzerManualState) {
      buzzerManualState = false;
      Serial.println("Button Pressed: Buzzer OFF");
    }
  }

  lastButtonState = reading;

  // Fire detection logic
  if (mq2Value > fireThreshold || buzzerManualState) {
    digitalWrite(buzzerPin, HIGH);
  } else {
    digitalWrite(buzzerPin, LOW);
  }

  delay(100);
}
