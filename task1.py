# Before running the python script, you need to write and run the appropriate code in the arduino IDE
'''
#include <mcp342x>
MCP342x myADC;

list<int> valuesNPLC = { 1, 5, 10 };
int potPin = A0;
int pot Val;

void setup() {
    myADC.begin();
    pinMode(potPin, INPUT);
    Serial.begin(115200);
}

void loop() {
    for (int nplc : valuesNPLC) {
        myADC.setNPLC(nplc);
        potVal = analogRead(potPin);
        Serial.print(potVal);
        Serial.print(",");
        Serial.println(nplc);
    }
    delay(100)
}
'''


from serial import Serial
import time


arduinoData = Serial('com3', 115200)
voltage_coeff = 3.3 / 1024
time.sleep(2)

while True:
    while arduinoData.in_waiting == 0:
        pass
    data = arduinoData.readline()
    data = str(data, "utf-8")
    data.rstrip('\r\n').split(',')
    voltage = int(data[0]) * voltage_coeff
    print(f"Voltage: {round(voltage, 3)}V, NPLC: {int(data[1])}")
