# Network Port Scanner

A TCP-based network port scanner built in Python with CLI and GUI for the ST4017CMD Introduction to Programming coursework
Softwarica College / Coventry University.


---

## What It Does

This tool scans a range of TCP ports on a target IP address and 
reports whether each port is open, closed, or filtered. Results 
are displayed in real time and saved to a text file.

---

## Project Files

| File | Description |
|------|-------------|
| `port_scanner.py` | Core scanning logic and CLI interface |
| `gui.py` | Graphical user interface built with Tkinter |
| `test_scanner.py` | Unit tests using Python's unittest framework |
| `scan_results.txt` | Output file generated after each scan |

---

## Requirements

- Python 3.x
- No external libraries required.
- Uses Python standard library only
- Tkinter is included with Python on Windows and macOS
- On Linux, Tkinter may need to be installed separately (see below)

---

## Installation

### Windows
Python 3 includes everything needed by default.

1. Download Python from https://www.python.org/downloads/
2. During installation, make sure **Add Python to PATH** is ticked
3. Verify installation:
```bash
python --version
```

### macOS
Python 3 includes everything needed by default.

1. Download Python from https://www.python.org/downloads/
2. Or install using Homebrew:
```bash
brew install python3
```
3. Verify installation:
```bash
python3 --version
```

### Linux (Ubuntu / Debian)
Python 3 is usually pre-installed. Tkinter needs to be installed 
separately for the GUI version.
```bash
# Check Python version
python3 --version

# Install Tkinter if not already installed
sudo apt-get install python3-tk
```

For Fedora / RHEL:
```bash
sudo dnf install python3-tkinter
```

For Arch Linux:
```bash
sudo pacman -S tk
```

---

## How to Run

### Clone the Repository
```bash
git clone https://github.com/bipinlamsal8/Port_Scanner.git
cd Port_Scanner
```

---

### CLI Version

**Windows:**
```bash
python port_scanner.py
```

**macOS / Linux:**
```bash
python3 port_scanner.py
```

Follow the prompts to enter a target IP address and port range.

---

### GUI Version

**Windows:**
```bash
python gui.py
```

**macOS / Linux:**
```bash
python3 gui.py
```

Fill in the IP address and port range fields, then click Start Scan.

---

### Unit Tests

**Windows:**
```bash
python test_scanner.py
```

**macOS / Linux:**
```bash
python3 test_scanner.py
```

---

## Example Usage
```
Enter target IP address: 127.0.0.1
Enter start port (1-65535): 1
Enter end port (1-65535): 100

==================================================
Scanning 127.0.0.1 from port 1 to 100
==================================================

Scan Complete
Total ports scanned: 100
Scan duration: 100.86 seconds
Results saved to scan_results.txt
```

---

## Features

- TCP connect scanning using Python's socket module
- Real-time progress display in CLI
- Input validation for IP address and port range
- Service name identification for known ports
- Saves results to scan_results.txt
- Graphical interface with scrollable output
- Background threading in GUI to prevent freezing
- Unit tested with 6 test cases which all passed

---

## Ethical Notice

This tool was developed and tested exclusively on localhost 
(127.0.0.1). Scanning external systems or networks without 
explicit authorisation is illegal. This project is strictly 
for educational purposes.

---

## Version Control

This project was developed incrementally using Git with 50+ commits
documenting the full development process including bug fixes, 
GUI implementation, and unit testing.

---

## Author

- **Name:** Bipin Lamsal
- **Student ID:** 250510 / 17106562
- **Module:** ST4017CMD Introduction to Programming
- **Institution:** Softwarica College of IT & E-Commerce in 
  collaboration with Coventry University
