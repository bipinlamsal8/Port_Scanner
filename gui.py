import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from port_scanner import scan_single_port, validate_ip, validate_port, scan_port_range, PortResult
import time

def start_scan():

    if not validate_ip(target):
        messagebox.showerror("Error", "Invalid IP address")
        return

    try: 
        start_port = int(entry_start.get())
        end_port = int(entry_end.get())

        if not validate_port(start_port) or not validate_port(end_port):
            messagebox.showerror("Error", "Ports must be between 1 and 65535")
            return

        if start_port > end_port:
            messagebox.showerror("Error", "Start port must be <= end port")
            return

        output_text.delete(1.0, tk.END) 
        output_text.insert(tk.END, f"Scanning {target}...\n\n")

        start_time = time.time()            