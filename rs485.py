print("Sensors and Actuators")

import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
    # return "/dev/ttyUSB1"

portName = getPort()
print(portName)



try:
    ser = serial.Serial(port=portName, baudrate=9600)
    print("Open successfully")
except:
    print("Can not open the port")

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print("Array:", data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0


relay_ON = [                                                                                                                                  
      None,
      [1, 6, 0, 0, 0, 255, 201, 138],  # Relay 1 ON
      [2, 6, 0, 0, 0, 255, 201, 185],  # Relay 2 ON
      [3, 6, 0, 0, 0, 255, 200, 104],  # Relay 3 ON
      [4, 6, 0, 0, 0, 255, 201, 223],  # Relay 4 ON
      [5, 6, 0, 0, 0, 255, 200, 14],   # Relay 5 ON
      [6, 6, 0, 0, 0, 255, 200, 61],   # Relay 6 ON
      [7, 6, 0, 0, 0, 255, 201, 236],  # Relay 7 ON
      [8, 6, 0, 0, 0, 255, 201, 19],    # Relay 8 ON,
    ]                                                                                                                                                  
                                                                                                                                                       
relay_OFF = [                                                                                                                                 
      None,
      [1, 6, 0, 0, 0, 0, 137, 202],    # Relay 1 OFF
      [2, 6, 0, 0, 0, 0, 137, 249],    # Relay 2 OFF
      [3, 6, 0, 0, 0, 0, 136, 40],     # Relay 3 OFF
      [4, 6, 0, 0, 0, 0, 137, 159],    # Relay 4 OFF
      [5, 6, 0, 0, 0, 0, 136, 78],     # Relay 5 OFF
      [6, 6, 0, 0, 0, 0, 136, 125],    # Relay 6 OFF
      [7, 6, 0, 0, 0, 0, 137, 172],    # Relay 7 OFF
      [8, 6, 0, 0, 0, 0, 137, 83]      # Relay 8 OFF
          ]

def setDevice(id, state):
    if state == True:
        print(relay_ON[id], "--------")
        ser.write(relay_ON[id])
    else:
        print(relay_OFF[id], "--------")
        ser.write(relay_OFF[id])
    time.sleep(1)
    print("Result: ", serial_read_data(ser))

# while True:
#     for i in range(1,8):
#         setDevice(i, True)
#         time.sleep(2)
#         setDevice(i, False)
#         time.sleep(2)

soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)

# while True:
#     print("TEST SENSOR")
#     print(readMoisture())
#     time.sleep(1)
#     print(readTemperature())
#     time.sleep(1)