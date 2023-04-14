
#include "I2Cdev.h"
#include "MPU6050.h"

// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;

#define OUTPUT_READABLE_ACCELGYRO

const int FLEX_PIN_1 = A1;
const int FLEX_PIN_2 = A2;
const int FLEX_PIN_3 = A3;

#define PIR_PIN_1 4
#define PIR_PIN_2 7


void setup() {
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif
    Serial.begin(9600);
    // initialize device
    Serial.println("Initializing I2C devices...");
    accelgyro.initialize();
    // verify connection
    Serial.println("Testing device connections...");
    Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");

    pinMode(FLEX_PIN_1, INPUT);
    pinMode(FLEX_PIN_2, INPUT);
    pinMode(FLEX_PIN_3, INPUT);

    pinMode(PIR_PIN_1, INPUT);
    pinMode(PIR_PIN_2, INPUT);

    // Serial.println("Waiting 15 Seconds while PIR warms up");
    // for (uint8_t seconds = 0; seconds < 15; seconds++)
    // {
    //   Serial.println(seconds);
    //   delay(1000);
    // }
    // Serial.println("PIR Warmed up.");
}

void loop() {
    // read raw accel/gyro measurements from device
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    int flex1 = analogRead(FLEX_PIN_1);
    int flex2 = analogRead(FLEX_PIN_2);
    int flex3 = analogRead(FLEX_PIN_3);

    int PIR_1 = digitalRead(PIR_PIN_1);
    int PIR_2 = digitalRead(PIR_PIN_2);

    #ifdef OUTPUT_READABLE_ACCELGYRO
        Serial.print(ax); 
        Serial.print(" ");
        Serial.print(ay); 
        Serial.print(" ");
        Serial.print(az); 
        Serial.print(" ");
        Serial.print(gx); 
        Serial.print(" ");
        Serial.print(gy); 
        Serial.print(" ");
        Serial.print(gz);
        Serial.print(" ");
        Serial.print(flex1);
        Serial.print(" ");
        Serial.print(flex2);
        Serial.print(" ");
        Serial.print(flex3);
        Serial.print(" ");
        Serial.print(PIR_1);
        Serial.print(" ");
        Serial.println(PIR_2);

    #endif

    delay(30);
}
