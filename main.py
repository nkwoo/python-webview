import webview
import ctypes
import keyboard
import configparser
import sys 

config = configparser.ConfigParser()
config.read('./url.ini')
url = config['SETTING']['URL']

firstKey = False
inputKey = False
command = ""

def check_exit(key):
    global inputKey, command
    if inputKey == True:
        if key == "esc":
            inputKey = False
        else:
            if len(command) < 10:
                command = command + key
            
    else:
        if key == "esc":
            inputKey = True
            command = ""
        else:
            inputKey = False
    return command

def print_pressed_keys(e):
    global firstKey
    for code in keyboard._pressed_events:
        line = ', '.join(str(code))

        command = check_exit(e.name)

        if command == "exit":
            window.destroy()

def destroy_check(window):
    keyboard.hook(print_pressed_keys)

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

window = webview.create_window("WebView", url, "", None, screen_width, screen_height, None, None, False, True, (100, 100), False, False, False, True)
webview.start(destroy_check, window, {}, "cef")

