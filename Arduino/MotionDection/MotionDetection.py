# MotionDetection.py - this script will manage the motion detection system on the arduino uno board.
# Developer: Brandon M. Hunter
# Date: 12.15.18

# Import required libraries
import pyfirmata
from time import sleep

# Define custom function to perform Blink function
def blinkLED(pin, message):
    print(message)
    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(1)

# Associate port and board with pyFirmata
print("Associating port with board")
port  = "COM3" #'/dev/ttyACM0'
board = pyfirmata.Arduino(port)
print("Completed")
# Use iterator thread to avoid buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()
print("Define pins")
# Define pins
pirPin   = board.get_pin('d:7:i')
redPin   = 12
greenPin = 13
print("Completed")
# Check for PIR sensor input
print("Enter loop")
while True:
      # Ignore case when receiving None value from pin
      value  = pirPin.read() # does not recongize this ping.
      print("Value: {}".format(value))
      while value is None:
         pass
      print("Check if the value is true or false.")
      if value is True:
         # Perform Blink using custom function
         blinkLED(redPin, "Motion Detected")
      else:
          blinkLED(greenPin, "No motion Detected")

      print("Checked completed") 

# Release the board
board.exit()