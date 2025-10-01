import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import socket
import threading
import os
import platform
import json

class FileTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform File Transfer")
        self.root.geometry("600x500")
        
        # Platform info
        self.platform_info = f"{platform.system()} {platform.release()}"
        
        # Server socket
        self.server_socket = None
        self.is_server_running = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="File Transfer Tool", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Platform info
        platform_label = tk.Label(self.root, text=f"Platform: {self.platform_info}")
        platform_label.pack()
        
        # Notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Send tab
        send_frame = ttk.Frame(notebook)
        notebook.add(send_frame, text="Send File")
        self.setup_send_tab(send_frame)
        
        # Receive tab
        receive_frame = ttk.Frame(notebook)
        notebook.add(receive_frame, text="Receive File")
        self.setup_receive_tab(receive_frame)
        
    def setup_send_tab(self, parent):
        # File selection
        file_frame = ttk.LabelFrame(parent, text="File Selection", padding=10)
        file_frame.pack(fill='x', padx=10, pady=10)
        
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(file_frame, textvariable=self.file_path_var, state='readonly')
        file_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_file)
        browse_btn.pack(side='right')
        
        # Connection settings
        conn_frame = ttk.LabelFrame(parent, text="Connection", padding=10)
        conn_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(conn_frame, text="Target IP:").grid(row=0, column=0, sticky='w', pady=5)
        self.target_ip_var = tk.StringVar(value="127.0.0.1")
        ttk.Entry(conn_frame, textvariable=self.target_ip_var).grid(row=0, column=1, sticky='ew', pady=5)
        
        ttk.Label(conn_frame, text="Port:").grid(row=1, column=0, sticky='w', pady=5)
        self.send_port_var = tk.StringVar(value="5000")
        ttk.Entry(conn_frame, textvariable=self.send_port_var).grid(row=1, column=1, sticky='ew', pady=5)
        
        conn_frame.columnconfigure(1, weight=1)
        
        # Send button
        send_btn = ttk.Button(parent, text="Send File", command=self.send_file)
        send_btn.pack(pady=10)
        
        # Status
        self.send_status_var = tk.StringVar(value="Ready to send")
        status_label = ttk.Label(parent, textvariable=self.send_status_var, 
                                foreground="blue")
        status_label.pack(pady=5)
        
    def setup_receive_tab(self, parent):
        # Server settings
        server_frame = ttk.LabelFrame(parent, text="Server Settings", padding=10)
        server_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(server_frame, text="Listen Port:").grid(row=0, column=0, sticky='w', pady=5)
        self.recv_port_var = tk.StringVar(value="5000")
        ttk.Entry(server_frame, textvariable=self.recv_port_var).grid(row=0, column=1, sticky='ew', pady=5)
        
        server_frame.columnconfigure(1, weight=1)
        
        # Control buttons
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(pady=10)
        
        self.start_btn = ttk.Button(btn_frame, text="Start Server", command=self.start_server)
        self.start_btn.pack(side='left', padx=5)
        
        self.stop_btn = ttk.Button(btn_frame, text="Stop Server", command=self.stop_server, state='disabled')
        self.stop_btn.pack(side='left', padx=5)
        
        # Status
        self.recv_status_var = tk.StringVar(value="Server stopped")
        status_label = ttk.Label(parent, textvariable=self.recv_status_var, 
                                foreground="blue")
        status_label.pack(pady=5)
        
        # Save location
        save_frame = ttk.LabelFrame(parent, text="Save Location", padding=10)
        save_frame.pack(fill='x', padx=10, pady=10)
        
        self.save_path_var = tk.StringVar(value=os.path.expanduser("~"))
        save_entry = ttk.Entry(save_frame, textvariable=self.save_path_var, state='readonly')
        save_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        browse_save_btn = ttk.Button(save_frame, text="Browse", command=self.browse_save_location)
        browse_save_btn.pack(side='right')
        
    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_path_var.set(filename)
            
    def browse_save_location(self):
        directory = filedialog.askdirectory()
        if directory:
            self.save_path_var.set(directory)
            
    def send_file(self):
        file_path = self.file_path_var.get()
        if not file_path:
            messagebox.showwarning("No File", "Please select a file to send")
            return
            
        target_ip = self.target_ip_var.get()
        try:
            port = int(self.send_port_var.get())
        except ValueError:
            messagebox.showerror("Invalid Port", "Please enter a valid port number")
            return
            
        thread = threading.Thread(target=self._send_file_thread, 
                                 args=(file_path, target_ip, port))
        thread.daemon = True
        thread.start()
        
    def _send_file_thread(self, file_path, target_ip, port):
        try:
            self.send_status_var.set("Connecting...")
            
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((target_ip, port))
            
            # Send file metadata
            filename = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            metadata = json.dumps({"filename": filename, "size": file_size})
            client_socket.send(metadata.encode() + b"\n")
            
            # Send file data
            self.send_status_var.set(f"Sending {filename}...")
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    client_socket.send(data)
                    
            client_socket.close()
            self.send_status_var.set(f"File sent successfully!")
            
        except Exception as e:
            self.send_status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Send Error", str(e))
            
    def start_server(self):
        try:
            port = int(self.recv_port_var.get())
        except ValueError:
            messagebox.showerror("Invalid Port", "Please enter a valid port number")
            return
            
        self.is_server_running = True
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
        thread = threading.Thread(target=self._server_thread, args=(port,))
        thread.daemon = True
        thread.start()
        
    def _server_thread(self, port):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('0.0.0.0', port))
            self.server_socket.listen(5)
            self.server_socket.settimeout(1.0)
            
            self.recv_status_var.set(f"Server listening on port {port}...")
            
            while self.is_server_running:
                try:
                    client_socket, addr = self.server_socket.accept()
                    self.recv_status_var.set(f"Connection from {addr[0]}...")
                    
                    # Receive metadata
                    metadata_bytes = b""
                    while b"\n" not in metadata_bytes:
                        metadata_bytes += client_socket.recv(1024)
                    
                    metadata = json.loads(metadata_bytes.decode().strip())
                    filename = metadata["filename"]
                    file_size = metadata["size"]
                    
                    # Receive file
                    save_path = os.path.join(self.save_path_var.get(), filename)
                    self.recv_status_var.set(f"Receiving {filename}...")
                    
                    received = 0
                    with open(save_path, 'wb') as f:
                        while received < file_size:
                            data = client_socket.recv(4096)
                            if not data:
                                break
                            f.write(data)
                            received += len(data)
                            
                    client_socket.close()
                    self.recv_status_var.set(f"Received {filename}!")
                    messagebox.showinfo("File Received", f"File saved to:\n{save_path}")
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.is_server_running:
                        self.recv_status_var.set(f"Error: {str(e)}")
                        
        except Exception as e:
            self.recv_status_var.set(f"Server error: {str(e)}")
            messagebox.showerror("Server Error", str(e))
        finally:
            if self.server_socket:
                self.server_socket.close()
            self.start_btn.config(state='normal')
            self.stop_btn.config(state='disabled')
            
    def stop_server(self):
        self.is_server_running = False
        self.recv_status_var.set("Stopping server...")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FileTransferApp(root)
    root.mainloop()
