# Cross-Platform File Transfer Tool

A simple and intuitive desktop file transfer application built with Python and Tkinter. This tool allows you to send and receive files over a local network or the internet between Windows, Linux, and macOS systems.

## Features

- **Cross-Platform Compatibility**: Works seamlessly on Windows, Linux, and macOS
- **Simple GUI**: User-friendly interface built with Tkinter
- **Two-Way Transfer**: Send and receive files from the same application
- **No External Dependencies**: Uses only Python standard library modules
- **Real-Time Status**: View connection and transfer status in real-time
- **Customizable**: Configure IP addresses and ports for your network setup

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python installations)

## Installation

1. Clone or download this repository
2. Ensure Python 3.6+ is installed on your system
3. No additional packages need to be installed!

## Usage

### Running the Application

```bash
python main.py
```

### Sending Files

1. Switch to the "Send File" tab
2. Click "Browse" to select the file you want to send
3. Enter the target IP address of the receiving computer
4. Set the port number (default: 5000)
5. Click "Send File"

### Receiving Files

1. Switch to the "Receive File" tab
2. Set the port number to listen on (default: 5000)
3. (Optional) Click "Browse" to change the save location
4. Click "Start Server"
5. Wait for incoming file transfers
6. Click "Stop Server" when done

## How It Works

The application uses TCP sockets to establish connections between computers:

- The **receiving computer** runs a server that listens for incoming connections
- The **sending computer** connects to the receiver's IP address and port
- File metadata (name and size) is sent first
- The actual file data is then transferred in chunks

## Platform Support

- **Windows**: Fully supported (Windows 7 and later)
- **Linux**: Fully supported (most distributions)
- **macOS**: Fully supported (macOS 10.12 and later)

## Security Notes

⚠️ **Important**: This tool is designed for use on trusted networks. It does not include:
- Encryption
- Authentication
- Authorization

For secure file transfers over untrusted networks, consider using additional security measures.

## Troubleshooting

### Firewall Issues
If you cannot connect:
1. Check that the receiving computer's firewall allows incoming connections on the specified port
2. On Windows: Allow Python through Windows Firewall
3. On Linux: Configure iptables or ufw to allow the port
4. On macOS: Check System Preferences > Security & Privacy > Firewall

### Network Issues
- Ensure both computers are on the same network or can reach each other via internet
- Use the correct IP address (use `ipconfig` on Windows or `ifconfig`/`ip addr` on Linux/macOS to find it)
- Avoid using 127.0.0.1 (localhost) when transferring between different computers

## License

This project is open source and available for personal and educational use.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Created as a demonstration of cross-platform Python development with Tkinter.
