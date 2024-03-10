from pico_hid.ascii_to_hid import HID_KEY_SHIFT_LEFT
from pico_hid.ascii_to_hid import conv_table
from pico_hid.ascii_to_hid import key_mappings
from pico_hid.serial_com import send


# Function to convert ASCII characters to HID keycodes
def ascii_to_hid(key: str):
    if key in key_mappings:
        return 0, key_mappings[key]
    elif len(key) == 1:
        ascii_val = ord(key)  # Get ASCII value of character
        if ascii_val < len(
            conv_table
        ):  # Check if the ASCII value is within the range of the conversion table
            shift, keycode = conv_table[ascii_val]
            return shift, keycode
    else:
        return None


def press(key: str):
    result = ascii_to_hid(key)
    if result is not None:
        shift, keycode = result
        if shift:
            send(f"keyboard_press,{HID_KEY_SHIFT_LEFT}\n")
        send(f"keyboard_press,{keycode}\n")


def release(key: str):
    result = ascii_to_hid(key)
    if result is not None:
        shift, keycode = result
        if shift:
            send(f"keyboard_release,{HID_KEY_SHIFT_LEFT}\n")
        send(f"keyboard_release,{keycode}\n")


def release_all():
    send("keyboard_release\n")


def press_and_release(key: str):
    result = ascii_to_hid(key)
    if result is not None:
        shift, keycode = result
        if shift:
            send(f"keyboard_press,{HID_KEY_SHIFT_LEFT}\n")
        send(f"keyboard_keystroke,{keycode}\n")
        if shift:
            send(f"keyboard_release,{HID_KEY_SHIFT_LEFT}\n")


def write(text: str):
    for char in text:
        press_and_release(char)
