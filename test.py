from serial import Serial

from pico_hid.keyboard import Keyboard

# from pico_hid.mouse import Mouse
# from pico_hid.mouse import MouseButton


# Initialize serial port
ser = Serial("COM5", 115200)

# # Initialize mouse and keyboard
# mouse = Mouse(ser)

# # Example usage
# mouse.press(MouseButton.RIGHT)
# time.sleep(10)
# mouse.release()

keyboard = Keyboard(ser)
keyboard.press_and_release(":")
