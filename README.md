# 🚀 Cross-Platform File Transfer

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![OS](https://img.shields.io/badge/os-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Stars](https://img.shields.io/github/stars/rahit91890/file-transfer-cross-platform?style=social)](https://github.com/rahit91890/file-transfer-cross-platform/stargazers)

> **A simple, intuitive, and cross-platform file transfer solution** - Send and receive files seamlessly across Windows, Linux, and macOS with an elegant GUI interface.

---

## ✨ Features

- 🌐 **Cross-Platform Compatibility** - Works seamlessly on Windows, Linux, and macOS
- 🎨 **Simple GUI** - User-friendly interface built with Tkinter
- ↔️ **Two-Way Transfer** - Send and receive files from the same application
- 📦 **Zero External Dependencies** - Uses only Python standard library modules
- ⚡ **Real-Time Status** - View connection and transfer status in real-time
- 🔧 **Customizable** - Configure IP addresses and ports for your network setup
- 🚀 **Fast & Reliable** - TCP socket-based file transfer with chunked transmission

---

## 📋 Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python installations)

---

## 🔧 Installation

**Clone the repository:**

```bash
git clone https://github.com/rahit91890/file-transfer-cross-platform.git
cd file-transfer-cross-platform/desktop
```

**Ensure Python 3.6+ is installed:**

```bash
python --version
```

**No additional packages need to be installed!**

---

## 🚀 Usage

### Running the Application

```bash
cd desktop
python main.py
```

### 📤 Sending Files

1. Switch to the **"Send File"** tab
2. Click **"Browse"** to select the file you want to send
3. Enter the **target IP address** of the receiving computer
4. Set the **port number** (default: 5000)
5. Click **"Send File"**

### 📥 Receiving Files

1. Switch to the **"Receive File"** tab
2. Set the **port number** to listen on (default: 5000)
3. (Optional) Click **"Browse"** to change the save location
4. Click **"Start Server"**
5. Wait for incoming file transfers
6. Click **"Stop Server"** when done

---

## 🔍 How It Works

The application uses **TCP sockets** to establish connections between computers:

1. 🖥️ The **receiving computer** runs a server that listens for incoming connections
2. 📡 The **sending computer** connects to the receiver's IP address and port
3. 📝 File **metadata** (name and size) is sent first
4. 📦 The actual **file data** is then transferred in chunks for reliability

```
Sender                    Network                    Receiver
  |                          |                           |
  |-------- Connect -------->|----------- ACK --------->|
  |                          |                           |
  |---- Send Metadata ------>|------ File Info -------->|
  |                          |                           |
  |---- Transfer Data ------>|------ File Data -------->|
  |                          |                           |
  |------- Complete -------->|------- Success --------->|
```

---

## 💻 Platform Support

| Platform | Status | Minimum Version |
|----------|--------|----------------|
| 🪟 **Windows** | ✅ Fully Supported | Windows 7+ |
| 🐧 **Linux** | ✅ Fully Supported | Most distributions |
| 🍎 **macOS** | ✅ Fully Supported | macOS 10.12+ |

---

## 🔒 Security Notes

⚠️ **Important:** This tool is designed for use on **trusted networks**. It does not include:

- 🔐 Encryption
- 🔑 Authentication
- 🛡️ Authorization

For secure file transfers over untrusted networks, consider using additional security measures such as VPN or SSH tunneling.

---

## 🛠️ Troubleshooting

### 🔥 Firewall Issues

If you cannot connect:

1. Check that the receiving computer's firewall allows incoming connections on the specified port
2. **Windows:** Allow Python through Windows Firewall
3. **Linux:** Configure `iptables` or `ufw` to allow the port:
   ```bash
   sudo ufw allow 5000
   ```
4. **macOS:** Check System Preferences → Security & Privacy → Firewall

### 🌐 Network Issues

- Ensure both computers are on the same network or can reach each other via internet
- Use the correct IP address:
  - **Windows:** `ipconfig`
  - **Linux/macOS:** `ifconfig` or `ip addr`
- Avoid using `127.0.0.1` (localhost) when transferring between different computers

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/rahit91890/file-transfer-cross-platform/issues).

**Steps to contribute:**

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project is open source and available for personal and educational use.

---

## 👨‍💻 Author

**Created by [rahit91890](https://github.com/rahit91890)**

Demonstrating cross-platform Python development with Tkinter and socket programming.

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

[![GitHub Stars](https://img.shields.io/github/stars/rahit91890/file-transfer-cross-platform?style=social)](https://github.com/rahit91890/file-transfer-cross-platform/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/rahit91890/file-transfer-cross-platform?style=social)](https://github.com/rahit91890/file-transfer-cross-platform/network/members)

---

<div align="center">
  <p><strong>Made with ❤️ and Python</strong></p>
  <p>⭐ <a href="https://github.com/rahit91890/file-transfer-cross-platform">Star this repo</a> | 🍴 <a href="https://github.com/rahit91890/file-transfer-cross-platform/fork">Fork it</a> | 🐛 <a href="https://github.com/rahit91890/file-transfer-cross-platform/issues">Report bugs</a></p>
</div>
