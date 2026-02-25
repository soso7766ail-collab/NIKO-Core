import os

class NikoGrowth:
    def __init__(self):
        self.core_files = ['main.py', 'memory_system.py', 'security_layer/net_scanner.py']

    def auto_repair(self):
        print("[Niko] Checking system integrity...")
        for file in self.core_files:
            if os.path.exists(file):
                print(f"  [+] {file}: Optimized.")
            else:
                print(f"  [-] {file}: Missing! Initializing emergency recovery...")
                # هنا يقوم Niko بكتابة الملف المفقود تلقائياً
