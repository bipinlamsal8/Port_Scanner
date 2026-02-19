import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from port_scanner import scan_single_port, validate_ip, validate_port, scan_port_range, PortResult
import time

def start_scan():

    if not validate_ip(target):
        messagebox.showerror("Error", "Invalid IP address")
        return