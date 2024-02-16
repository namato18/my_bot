import time
import serial
import keyboard

# open coms
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5.0)
time.sleep(2)
ser.reset_input_buffer()
print("Serial OK")

try:
    while True:
        if keyboard.is_pressed('w'):
            print('MOVE FORWARD')
            ser.write("forward\n".encode('utf-8'))
            time.sleep(0.1)
        elif keyboard.is_pressed('a'):
            print('MOVE LEFT')
            ser.write("left\n".encode('utf-8'))
            time.sleep(0.1)
        elif keyboard.is_pressed('s'):
            print('MOVE BACKWARD')
            ser.write("backward\n".encode('utf-8'))
            time.sleep(0.1)
        elif keyboard.is_pressed('d'):
            print('MOVE RIGHT')
            ser.write("right\n".encode('utf-8'))
            time.sleep(0.1)
        elif keyboard.is_pressed('x'):
            print('STOP')
            ser.write("stop\n".encode('utf-8'))
            time.sleep(0.1)
            





except KeyboardInterrupt:
    print("close serial coms")
    ser.close()

