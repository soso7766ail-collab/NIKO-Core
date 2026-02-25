import os
import sys
import platform
import datetime

class NikoKernel:
    def __init__(self):
        self.version = "1.0.0-Alpha"
        self.start_time = datetime.datetime.now()
        self.system_info = self.get_env_info()
        
    def get_env_info(self):
        # جمع معلومات البيئة المحيطة بنيكو
        return {
            "OS": platform.system(),
            "Release": platform.release(),
            "Machine": platform.machine(),
            "User": os.getlogin() if hasattr(os, 'getlogin') else "Termux_User"
        }

    def boot(self):
        print(f"--- [Niko Core System v{self.version}] ---")
        print(f"[*] Booting at: {self.start_time}")
        print(f"[*] Environment: {self.system_info['OS']} on {self.system_info['Machine']}")
        print("[+] Checking layers...")
        
        # التأكد من وجود المجلدات الأساسية
        layers = ['kernel_layer', 'cognition_core', 'memory_system', 'security_layer']
        for layer in layers:
            if os.path.exists(layer):
                print(f"  - {layer}: READY")
            else:
                print(f"  - {layer}: MISSING!")
        
        print("[!] Niko is now ONLINE.")

if __name__ == "__main__":
    niko = NikoKernel()
    niko.boot()
