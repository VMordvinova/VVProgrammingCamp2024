#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance.


// Define arrays for UIDs and corresponding names
const int NUM_MAPPINGS = 3;  // Adjust this to the number of mappings you have
String uids[NUM_MAPPINGS] = {"D3B23EFA", "833C27F7", "4379F534"};
String names[NUM_MAPPINGS] = {"Veronica", "Justin", "Emily"};

int pinLED = 2;
int pinLED2 = 7;

int readsuccess;
byte readcard[4];
char str[32] = "";
String StrUID;

void setup() {
  Serial.begin(9600); // Initialize serial communications with the PC
  SPI.begin();        // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card

  Serial.println("CLEARDATA");
  Serial.println("LABEL,Date,Time,RFID UID,NAME");
  delay(1000);

  Serial.println("Scan PICC to see UID...");
  Serial.println("");
}

//seeing what to do if the scan is successful
void loop() {
  readsuccess = getid();

  if (readsuccess) {
    String name = getNameForUID(StrUID);
    Serial.println((String) "DATA,DATE,TIME," + StrUID + "," + name);
  }
}

int getid() {
  if (!mfrc522.PICC_IsNewCardPresent()) {
    return 0;
  }
  if (!mfrc522.PICC_ReadCardSerial()) {
    //turns red LED on and off
    digitalWrite(pinLED, HIGH);
    delay(2000);
    digitalWrite(pinLED, LOW);
    return 0;
  }

  Serial.println("THE UID OF THE SCANNED CARD IS:");

  for (int i = 0; i < 4; i++) {
    readcard[i] = mfrc522.uid.uidByte[i]; // storing the UID of the tag in readcard
  }
  array_to_string(readcard, 4, str);
  StrUID = str;

  mfrc522.PICC_HaltA();
  //turns green LED on and off
  digitalWrite(pinLED2, HIGH);
  Serial.println();
  delay(2000);
  digitalWrite(pinLED2, LOW);

  return 1;
}

//getting the RFID UID to a string
void array_to_string(byte array[], unsigned int len, char buffer[]) {
  for (unsigned int i = 0; i < len; i++) {
    byte nib1 = (array[i] >> 4) & 0x0F;
    byte nib2 = (array[i] >> 0) & 0x0F;
    buffer[i * 2 + 0] = nib1 < 0xA ? '0' + nib1 : 'A' + nib1 - 0xA;
    buffer[i * 2 + 1] = nib2 < 0xA ? '0' + nib2 : 'A' + nib2 - 0xA;
  }
  buffer[len * 2] = '\0';
}

//finding the corresponding name for the RFID id
String getNameForUID(String uid) {
  for (int i = 0; i < NUM_MAPPINGS; i++) {
    if (uids[i] == uid) {
      return names[i];
    }
  }
  return "Unknown";  // Return "Unknown" if the UID is not found
}