from wiimote import Wiimote
import cwiid

wii = Wiimote()
wii.connect_wiimote()
wii.connection_fun()

while True:
 
  buttons = wii.get_buttons()
 
  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    exit(wii)
 
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time.sleep(button_delay)
 
  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)