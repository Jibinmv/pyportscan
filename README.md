# 🔐 PyPortScan — Python TCP Port Scanner

A lightweight and beginner-friendly **TCP Port Scanner built with Python** using the built-in `socket` module.

PyPortScan scans a specified range of TCP ports on an authorized target, identifies open ports, attempts to determine the associated service, displays real-time scan progress, and generates a final scan report.

> ⚠️ **For educational and authorized security testing only.**
> Only scan systems, devices, and networks that you own or have explicit permission to test.

---

## 🚀 Features

- 🔍 TCP port scanning
- 🎯 Custom target IP/hostname
- 🔢 Custom start and end port
- ⚡ Socket-based TCP connection testing
- 🛠️ Basic service identification
- 📊 Real-time scanning progress bar
- ⏱️ Scan execution time measurement
- 📋 Final scan report
- 🖥️ Simple command-line interface
- 🐍 Built completely with Python standard libraries

---

## 🧰 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Socket | TCP connection and port scanning |
| Time | Scan timing and performance measurement |
| `getservbyport()` | Basic service identification |

---

## 📂 Project Structure

```text
pyportscan/
│
├── Port_Scanner.py
└── README.md
