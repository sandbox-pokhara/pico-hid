import time
from enum import Enum

from serial import Serial


class MouseButton(Enum):
    LEFT = "left"
    RIGHT = "right"


class Mouse:
    def __init__(self, serial_port: Serial):
        self.serial_port = serial_port

    def move(self, x: int, y: int):
        x_normalized = x * 32767 // 1920
        y_normalized = y * 32767 // 1080
        self.send(f"mouse_move,{x_normalized},{y_normalized}\n")

    def press(self, button: MouseButton):
        self.send(f"mouse_press_{button.value}\n")

    def release(self):
        self.send(f"mouse_release\n")

    def click(self, button: MouseButton):
        self.send(f"mouse_click_{button.value}\n")

    def send(self, command: str):
        self.serial_port.write(command.encode())
        time.sleep(0.1)  # Mandatory delay
        echoed_message = self.serial_port.readline().decode().strip()
        print("Echoed message:", echoed_message)
