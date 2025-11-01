# 🧵 Process Synchronization on a Virtual Simulation Tool

This project simulates core operating system concepts like **multithreading**, **process synchronization**, and **file I/O operations** using virtual users. Each thread acts as a user performing randomized file tasks (create, delete, write, copy) in a shared directory, with synchronization mechanisms ensuring thread safety and consistency.

---

## 🚀 Features

- Simulates multiple virtual users using Python threads  
- Demonstrates race conditions and thread-safe operations  
- Enforces file limits and realistic delays  
- Provides a clean GUI for control and monitoring  
- Logs all actions with timestamps for traceability  

---

## 🧠 Core Concepts Demonstrated

- Process Synchronization  
- Thread Safety  
- File System Operations  
- Resource Limiting  
- Event Control  
- Exception Handling  
- Simulation Modeling  

---

## 🛠️ Tools & Technologies

- **Python** – Core language for simulation logic  
- **Threading Module** – Powers concurrent virtual users  
- **OS & Shutil** – Handles file operations and directory management  
- **Random & Time** – Adds realistic behavior and delays  
- **CustomTkinter** – GUI for simulation control  
- **VS Code** – Development and debugging environment  

---

## 📂 Project Structure

```
virtual_files/           # Shared directory for file operations
utils/
  └── file_manager.py    # Helper functions for file handling
virtual_world.py         # Thread logic and simulation loop
file_operations.py       # Core file operation functions
gui_controller.py        # GUI interface for control and status
.gitignore               # Ignores pycache and compiled files
```

---

## 🧪 How It Works

Each thread:
1. Randomly selects an operation: create, delete, write, or copy  
2. Acquires a lock to safely access shared resources  
3. Performs the operation and logs the result  
4. Sleeps briefly to simulate real-world delays  

The simulation continues until stopped or until file limits are reached.

---

## 📦 Setup & Run

1. Clone the repo:
   ```bash
   git clone https://github.com/pitzapizza/Process-Synchronization-on-a-Virtual-Simulation-Tool.git
   cd Process-Synchronization-on-a-Virtual-Simulation-Tool
   ```

2. Install dependencies (if any):
   ```bash
   pip install customtkinter
   ```

3. Run the simulation:
   ```bash
   python virtual_world.py
   ```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Contributions

Feel free to fork, improve, or suggest enhancements via pull requests or issues. This project is built for learning and demonstration — let’s make it better together!  

---
