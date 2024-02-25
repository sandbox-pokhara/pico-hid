import time

from serial import Serial


class Keyboard:
    def __init__(self, serial_port: Serial):
        self.serial_port = serial_port

    def press(self, key: str):
        self.send(f"keyboard_press,{key}\n")

    def release(self, key: str):
        self.send(f"keyboard_release,{key}\n")

    def press_and_release(self, key: str):
        self.send(f"keyboard_keystroke,{key}\n")

    def write(self, text: str):
        self.send(f"keyboard_write,{text}\n")

    def send(self, command: str):
        self.serial_port.write(command.encode())
        time.sleep(0.1)  # Mandatory delay
        echoed_message = self.serial_port.readline().decode().strip()
        print("Echoed message:", echoed_message)
