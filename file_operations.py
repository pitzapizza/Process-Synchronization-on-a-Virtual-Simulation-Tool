import os, random, shutil, threading
from utils.file_manager import VIRTUAL_DIR

lock = threading.Lock()

def create_file(char_id):
    with lock:
        files = os.listdir(VIRTUAL_DIR)
        if len(files) >= 300:
            return f"{char_id} skipped file creation (limit reached)"
        filename = f"{char_id}_{random.randint(1000,9999)}.txt"
        path = os.path.join(VIRTUAL_DIR, filename)
        with open(path, "w") as f:
            f.write("")
        print(f"{char_id} created {filename}")
        return filename

def delete_file(char_id):
    with lock:
        files = os.listdir(VIRTUAL_DIR)
        if files:
            target = random.choice(files)
            os.remove(os.path.join(VIRTUAL_DIR, target))
            print(f"{char_id} deleted {target}")
            return target
        return f"{char_id} tried to delete but no files exist"

def write_file(char_id):
    with lock:
        files = os.listdir(VIRTUAL_DIR)
        if files:
            target = random.choice(files)
            with open(os.path.join(VIRTUAL_DIR, target), "a") as f:
                f.write(f"Data from {char_id}\n")
            print(f"{char_id} wrote to {target}")
            return target
        return f"{char_id} tried to write but no files exist"

def copy_file(char_id):
    with lock:
        files = os.listdir(VIRTUAL_DIR)
        if files:
            src = random.choice(files)
            dest = f"{src}_copy_{random.randint(100,999)}"
            shutil.copy(os.path.join(VIRTUAL_DIR, src), os.path.join(VIRTUAL_DIR, dest))
            print(f"{char_id} copied {src} to {dest}")
            return dest
        return f"{char_id} tried to copy but no files exist"