import os
import time

VIRTUAL_DIR = "virtual_files"

def setup_environment():
    os.makedirs(VIRTUAL_DIR, exist_ok=True)
    print(f"✅ Environment ready at ./{VIRTUAL_DIR}")

def cleanup_virtual_files():
    for filename in os.listdir(VIRTUAL_DIR):
        path = os.path.join(VIRTUAL_DIR, filename)
        for _ in range(3):
            try:
                if os.path.isfile(path):
                    os.remove(path)
                break
            except PermissionError:
                time.sleep(0.1)
    print("🧹 All virtual files deleted.")