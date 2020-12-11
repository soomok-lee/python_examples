'''
11. 나만의 단축키 만들기 simple
pynput
'''
# from pynput.keyboard import Key, Listener, KeyCode # pip install pynput

# def key_pressed(key):
#     print("Pressed {}".format(key))

# def key_released(key):
#     print("Released {}".format(key))

#     if key == Key.esc:
#         return False

# with Listener(on_press=key_pressed, on_release=key_released) as listener:
#     listener.join()
    
'''
12. 나만의 단축키 만들기 smart
pip install pypiwin32 # window
'''
from pynput.keyboard import Key, Listener, KeyCode # pip install pynput
import win32api

MY_HOT_KEYS = [
    {"function1":{Key.ctrl_l, Key.alt_l, KeyCode(char="n")}},
    {"function2":{Key.shift, Key.alt_l, KeyCode(char="b")}},
    {"function3":{Key.ctrl_l, Key.alt_l, KeyCode(char="g")}}
]

current_keys = set()

def function1():
    print("call function1")
    win32api.WinExec("calc.exe")

def function2():
    print("call function2")    
    win32api.WinExec("notepad.exe")

def function3():
    print("call function3")    
    win32api.WinExec("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def key_pressed(key):
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]
        
        if key in KEYS:
            current_keys.add(key)

            # checker = True
            # for k in KEYS:
            #     if k not in current_keys:
            #         checker = False
            #         break
            # if checker:
            #     function = eval(FUNCTION)
            #     function()

            # comprehension
            if all(k in current_keys for k in KEYS):
                function = eval(FUNCTION)
                function()

def key_released(key):
    print("Released {}".format(key))

    if key in current_keys:
        current_keys.remove(key)

    if key == Key.esc:
        return False

with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()
