import random, threading, time
from file_operations import create_file, delete_file, write_file, copy_file

CHARACTERS = [f"Character_{i}" for i in range(5000)]
ACTIONS = [create_file, delete_file, write_file, copy_file]

stop_event = threading.Event()
pause_event = threading.Event()

def character_behavior(char_id):
    while not stop_event.is_set():
        if pause_event.is_set():
            time.sleep(0.1)
            continue
        action = random.choice(ACTIONS)
        action(char_id)
        time.sleep(random.uniform(0.05, 0.2))

def start_simulation():
    stop_event.clear()
    pause_event.clear()
    threads = []
    active_characters = random.sample(CHARACTERS, k=300)
    for char_id in active_characters:
        t = threading.Thread(target=character_behavior, args=(char_id,))
        t.start()
        threads.append(t)
    return threads