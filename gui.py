import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from port_scanner import scan_single_port, validate_ip, validate_port, scan_port_range, PortResult
import time

def start_scan():
    target = entry_ip.get().strip()

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

        results = scan_port_range(target, start_port, end_port) 

        open_ports = 0

        for result in results:
            if result.status == "OPEN":
                output_text.insert(tk.END, result.display() + "\n")
                open_ports += 1

        end_time = time.time() 
        duration = end_time - start_time

        output_text.insert(tk.END, f"\nScan Complete\n")
        output_text.insert(tk.END, f"Open ports found: {open_ports}\n")
        output_text.insert(tk.END, f"Scan duration: {duration:.2f} seconds\n")

    except ValueError:
        messagebox.showerror("Error", "Invalid port number")


def save_results():
    content = output_text.get(1.0, tk.END)

    if not content.strip():
        messagebox.showwarning("Warning", "Nothing to save!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as f:
            f.write(content)
        messagebox.showinfo("Success", "Results saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Network Port Scanner")
root.geometry("600x500")

tk.Label(root, text="Target IP:").pack()
entry_ip = tk.Entry(root, width=30)
entry_ip.pack()
entry_ip.insert(0, "127.0.0.1")

tk.Label(root, text="Start Port:").pack()
entry_start = tk.Entry(root, width=30)
entry_start.pack()
entry_start.insert(0, "1")

tk.Label(root, text="End Port:").pack()
entry_end = tk.Entry(root, width=30)
entry_end.pack()
entry_end.insert(0, "100")

tk.Button(root, text="Start Scan", command=start_scan).pack(pady=5)
tk.Button(root, text="Save to File", command=save_results).pack(pady=5)

output_text = scrolledtext.ScrolledText(root, height=20)
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
