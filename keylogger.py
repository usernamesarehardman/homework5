import keyboard

def on_key_event(event):
    print(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}")

# Hook all key events
keyboard.hook(on_key_event)

# Block forever, like listener.join()
keyboard.wait()