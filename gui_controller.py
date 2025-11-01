import customtkinter as ctk
import threading
import os
from virtual_world import start_simulation, stop_event, pause_event
from utils.file_manager import setup_environment, cleanup_virtual_files
from file_operations import create_file, delete_file, write_file, copy_file

class SimulationGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🧠 OS Sync Simulation")
        self.geometry("400x450")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.simulation_threads = []

        self.title_label = ctk.CTkLabel(self, text="OS Synchronization Simulator", font=ctk.CTkFont(size=18, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        self.start_button = ctk.CTkButton(self, text="▶ Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self, text="⏹ Stop Simulation", command=self.stop_simulation, state="disabled")
        self.stop_button.pack(pady=10)

        self.pause_button = ctk.CTkButton(self, text="⏸ Pause Simulation", command=self.toggle_pause, state="disabled")
        self.pause_button.pack(pady=10)

        self.analysis_button = ctk.CTkButton(self, text="📊 Analysis Dashboard", command=self.show_dashboard)
        self.analysis_button.pack(pady=10)

        self.check_button = ctk.CTkButton(self, text="✅ Check Operations", command=self.check_operations)
        self.check_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="Status: Ready", font=ctk.CTkFont(size=14))
        self.status_label.pack(pady=(20, 10))

    def start_simulation(self):
        setup_environment()
        self.status_label.configure(text="Status: Running")
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.pause_button.configure(state="normal")

        def run_simulation():
            self.simulation_threads = start_simulation()

        threading.Thread(target=run_simulation, daemon=True).start()

    def stop_simulation(self):
        self.status_label.configure(text="Status: Stopping...")
        stop_event.set()
        for t in self.simulation_threads:
            t.join()
        cleanup_virtual_files()
        self.status_label.configure(text="Status: Stopped")
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.pause_button.configure(state="disabled")
        pause_event.clear()

    def toggle_pause(self):
        if pause_event.is_set():
            pause_event.clear()
            self.pause_button.configure(text="⏸ Pause Simulation")
            self.status_label.configure(text="Status: Running")
        else:
            pause_event.set()
            self.pause_button.configure(text="▶ Resume Simulation")
            self.status_label.configure(text="Status: Paused")

    def show_dashboard(self):
        file_count = len(os.listdir("virtual_files"))
        dashboard = ctk.CTkToplevel(self)
        dashboard.title("📊 Analysis Dashboard")
        dashboard.geometry("300x200")

        ctk.CTkLabel(dashboard, text=f"Current File Count: {file_count}", font=ctk.CTkFont(size=14)).pack(pady=10)
        ctk.CTkLabel(dashboard, text="Max Allowed: 300", font=ctk.CTkFont(size=12)).pack(pady=5)
        ctk.CTkLabel(dashboard, text="Simulation Status:", font=ctk.CTkFont(size=12)).pack(pady=5)
        status = "Paused" if pause_event.is_set() else "Running"
        ctk.CTkLabel(dashboard, text=status, font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)

    def check_operations(self):
        try:
            test_id = "Test_Op"
            create_file(test_id)
            write_file(test_id)
            copy_file(test_id)
            delete_file(test_id)
            self.status_label.configure(text="✅ All operations working")
        except Exception as e:
            self.status_label.configure(text=f"❌ Operation error: {e}")

if __name__ == "__main__":
    app = SimulationGUI()
    app.mainloop()