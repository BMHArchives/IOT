import pyfirmata

pin  = 13 # digit pin 13
port = "COM3" # serial port to connect to
boardType = "Arduino Uno"
print("Associating {} port with your {}".format(port, boardType))
board = pyfirmata.Arduino(port) # associate the port with the microcontroller board type
print("Associated {} port with your {}".format(port, boardType))
#print("Turning on your LED light")
#board.digital[pin].write(1)
#print("LED light should be turned on now.")
#print("Turning off your LED light")
#board.digital[pin].write(0)
#print("LED light turned off.")

stopLoop = False
while stopLoop == False:
      userResponse = input("Type 1 to turn on light or 0 to turn off light and then hit the enter key: ")
      if userResponse == '1':
         print("Turning on your LED light")
         board.digital[pin].write(1)
         print("LED light is on")
      elif userResponse == '0':
           print("Turning off your LED light")
           board.digital[pin].write(0)
           print("LED light is off")
      else:
          print("You've entred {}. Please enter in a valid response of either 1 or 0.".format(userResponse)) 
      
      print(board.digital[pin].read()) # displays the status of a pin.
      print("")        
             
    