import os
import shutil
import tkinter as tk
from tkinter import messagebox
import psutil  # you'll need to install this module: pip install psutil

def close_chrome():
    for process in psutil.process_iter():
        try:
            if process.name() == "chrome.exe":
                process.terminate()
        except:
            pass

def clear_chrome_cache():
    # Get user's appdata path
    appdata_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'Cache')

    # Check if path exists
    if os.path.exists(appdata_path):
        try:
            # Delete cache
            shutil.rmtree(appdata_path)
            messagebox.showinfo("Info", "Chrome cache cleared successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear Chrome cache. Error: {e}")
    else:
        messagebox.showerror("Error", "Chrome cache path not found. Make sure Chrome is installed for the current user.")

def on_confirm():
    result = messagebox.askquestion("Confirm", "Do you want to clear the Chrome cache?", icon='warning')
    if result == 'yes':
        close_chrome()
        clear_chrome_cache()

# GUI part
app = tk.Tk()
app.geometry("300x100")
app.title("Clear Chrome Cache")

label = tk.Label(app, text="Click the button to clear Chrome cache:")
label.pack(pady=10)

btn = tk.Button(app, text="Clear Cache", command=on_confirm)
btn.pack(pady=10)

app.mainloop()
